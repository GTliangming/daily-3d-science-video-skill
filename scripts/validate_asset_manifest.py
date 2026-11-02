#!/usr/bin/env python3
"""Validate a 3D asset register for required metadata and basic production hygiene.

This checks documentation completeness only. It does NOT determine whether a
license is legally sufficient or whether a 3D model is geometrically correct.
"""
import json
import sys
from pathlib import Path

ALLOWED_PRIORITY = {"A", "B", "C", "D"}
ALLOWED_METHOD = {"download", "download_modify", "custom_model", "defer"}
ALLOWED_LICENSE_STATUS = {"CLEAR", "BLOCKED", "NEEDS_REVIEW"}
ALLOWED_COMMERCIAL = {"allowed", "not_allowed", "unclear"}
ALLOWED_MODIFICATION = {"allowed", "not_allowed", "unclear"}
ALLOWED_FORMATS = {"BLEND", "GLB", "GLTF", "FBX", "OBJ", "STL", "STEP", "OTHER"}


def validate(data):
    errors, warnings = [], []
    if not isinstance(data, dict):
        return ["根节点必须是 JSON 对象"], warnings
    if not isinstance(data.get("assets"), list) or not data["assets"]:
        return ["assets 必须是非空数组"], warnings

    seen = set()
    for index, asset in enumerate(data["assets"]):
        prefix = f"assets[{index}]"
        if not isinstance(asset, dict):
            errors.append(f"{prefix} 必须是对象")
            continue
        for field in ("asset_id", "name_zh", "category", "priority",
                      "production_method", "license_status", "format"):
            if not asset.get(field):
                errors.append(f"{prefix}.{field} 不能为空")
        asset_id = asset.get("asset_id")
        if asset_id:
            if asset_id in seen:
                errors.append(f"{prefix}.asset_id 重复：{asset_id}")
            seen.add(asset_id)
        if asset.get("priority") not in ALLOWED_PRIORITY:
            errors.append(f"{prefix}.priority 必须为 A/B/C/D")
        if asset.get("production_method") not in ALLOWED_METHOD:
            errors.append(f"{prefix}.production_method 不合法")
        if asset.get("license_status") not in ALLOWED_LICENSE_STATUS:
            errors.append(f"{prefix}.license_status 不合法")
        if asset.get("format") not in ALLOWED_FORMATS:
            errors.append(f"{prefix}.format 不合法")

        method = asset.get("production_method")
        status = asset.get("license_status")
        if method in {"download", "download_modify"}:
            for field in ("source_url", "creator", "license_name", "license_url"):
                if not asset.get(field):
                    errors.append(f"{prefix}.{field}：下载资产必须填写")
            if asset.get("commercial_use") not in ALLOWED_COMMERCIAL:
                errors.append(f"{prefix}.commercial_use 不合法或缺失")
            if asset.get("modification") not in ALLOWED_MODIFICATION:
                errors.append(f"{prefix}.modification 不合法或缺失")
            if status != "CLEAR":
                errors.append(f"{prefix}：下载资产许可未 CLEAR，禁止进入正式成片")
        elif method == "custom_model":
            if status != "CLEAR":
                errors.append(f"{prefix}：自建资产也必须确认权属/许可状态")

        if asset.get("attribution_required") and not asset.get("attribution_text"):
            errors.append(f"{prefix}.attribution_text：要求署名但未填写署名文本")
        dims = asset.get("dimensions_m")
        if dims is not None:
            if (not isinstance(dims, list) or len(dims) != 3
                    or any(not isinstance(v, (int, float)) or v <= 0 for v in dims)):
                errors.append(f"{prefix}.dimensions_m 必须是三个正数")
        elif asset.get("priority") in {"A", "B"}:
            warnings.append(f"{prefix}.dimensions_m 未填写，关键/主体资产建议记录尺寸")
        if not asset.get("file_path") and method != "defer":
            warnings.append(f"{prefix}.file_path 未填写")
    return errors, warnings


def main():
    if len(sys.argv) != 2:
        print("用法：python scripts/validate_asset_manifest.py <asset-register.json>")
        return 2
    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"无法读取 JSON：{exc}")
        return 2
    errors, warnings = validate(data)
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        print(f"FAIL：{len(errors)} 个错误，{len(warnings)} 个提醒")
        return 1
    print(f"PASS：资产登记结构有效（{len(data['assets'])} 项），{len(warnings)} 个提醒")
    print("注意：本工具不判断许可证的法律效力，也不检查模型几何质量。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
