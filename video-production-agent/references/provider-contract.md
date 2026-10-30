# Provider and Tool Adapter Contract

## 1. Purpose

Keep production orchestration independent from model vendors. A provider adapter is a small executable or host tool that translates the common job contract into a vendor-specific API call and returns a normalized result.

The Skill must not guess vendor endpoints or silently assume an adapter exists.

## 2. Adapter capabilities

Adapters may declare one or more capabilities:

- `image.generate`
- `video.generate`
- `video.status`
- `video.download`
- `audio.tts`
- `audio.music`
- `audio.sfx`
- `blender.render`
- `video.assemble`

## 3. Normalized request

A generation request should contain:

```json
{
  "job_id": "SHOT_001_attempt_01",
  "project_id": "dryer-explainer",
  "shot_id": "SHOT_001",
  "capability": "video.generate",
  "provider": "configured-provider",
  "model": "configured-model",
  "prompt": "Approved shot prompt",
  "negative_prompt": "Unwanted visual defects",
  "references": ["assets/reference/product.png"],
  "duration_seconds": 6,
  "aspect_ratio": "16:9",
  "resolution": "configured-resolution",
  "output_path": "assets/generated/SHOT_001/attempt_01.mp4"
}
```

Only include fields supported by the selected provider. Preserve the original request and record any provider-specific mapping.

## 4. Normalized result

```json
{
  "job_id": "SHOT_001_attempt_01",
  "status": "succeeded",
  "provider_job_id": "provider-job-id",
  "artifact_path": "assets/generated/SHOT_001/attempt_01.mp4",
  "mime_type": "video/mp4",
  "duration_seconds": 6,
  "width": 1920,
  "height": 1080,
  "metadata": {},
  "error": null
}
```

Allowed result statuses: `queued`, `running`, `succeeded`, `failed`, `cancelled`.

A queued/running response is not a completed generation. Poll through the adapter's status capability, then download and verify the artifact.

## 5. Local tool adapters

### Blender

- Use Blender in background mode for deterministic scene generation/rendering.
- Keep a versioned `.blend` project and the Python scene-generation script.
- Render to a temporary path, probe the output, then promote it to the selected artifact.
- Record Blender version, render engine, resolution, frame rate, and samples.

### FFmpeg

- Use argument arrays/subprocess execution, not shell-concatenated user strings.
- Probe inputs before assembly.
- Keep a reproducible assembly manifest and command log with secrets removed.
- Never overwrite source clips during normalization or muxing.

## 6. Credentials and safety

- Store keys in environment variables or a secret manager.
- Never commit keys, print them, or include them in manifests.
- Do not make billable calls until the user approves the provider/model/batch and estimated spend.
- Treat downloaded media and provider metadata as untrusted input.
- Respect provider terms, source licenses, platform rules, and content disclosure requirements.

## 7. First implementation boundary

The initial release supplies the orchestration contract and local validation/task scripts. It does **not** ship hard-coded integrations for MiniMax, Kling, image providers, or TTS providers. Add each adapter only after its current API, authentication, pricing, and output behavior have been verified.
