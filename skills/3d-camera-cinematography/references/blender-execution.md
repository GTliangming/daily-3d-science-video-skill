# Blender camera and shot execution

This guide turns a camera card into an inspectable Blender scene. It is version-aware: inspect the
installed Blender version and use its matching UI/API. Do not assume a specific version or silently
mix legacy and current APIs.

## 1. Scene preparation

Before camera work:
1. Confirm Blender version, render engine, frame rate, resolution and aspect ratio.
2. Confirm scene units and object scale; apply transforms when appropriate.
3. Confirm subject origin/pivot and the project's forward/up-axis convention.
4. Organize collections by responsibility, for example:
   - `ENVIRONMENT`
   - `SUBJECT`
   - `INTERNAL_PARTS`
   - `FX_AND_FLOW`
   - `CAMERAS`
   - `LIGHTS`
   - `GRAPHICS`
5. Name objects predictably: `CAM_S01_Main`, `RIG_S01_Target`, `LIGHT_Key`,
   `PRODUCT_Housing`, `PART_Motor`.
6. Keep source meshes and approved asset versions intact; use duplicates or linked collections
   for shot-specific changes.

## 2. Camera setup

- Add a camera and set it as the active scene camera.
- Set sensor fit and focal length deliberately; record the lens value and sensor assumptions.
- Place the camera based on the required perspective and composition, not by changing focal length
  alone.
- Aim with a target/rig object or a controlled rotation. Keep camera roll intentional.
- Use clipping distances that contain the subject without unnecessarily sacrificing depth
  precision.
- Use orthographic projection for technical diagrams only when its non-perspective look is desired.
- Check framing at the final output aspect ratio, not just the viewport default.

## 3. Recommended rig patterns

### Fixed camera / moving subject
Use for turntables, exploded components moving along known axes, or a product rotating for
inspection. Keep the camera locked and animate the subject or a dedicated parent rig. State clearly
that the object—not the camera—moves.

### Targeted dolly / push-in
Use a camera parented to a path or animate its position while a separate target controls aim.
Avoid scaling the camera or subject to fake a dolly.

### Orbit / arc
Use a path or controlled empty/pivot around the subject. Keep the target stable and inspect the
camera path for collisions and unwanted perspective changes. Do not assume a circular orbit is
appropriate for every object.

### Tracking / follow
Animate camera position and target together to preserve a defined screen-space relationship.
Avoid reactive gameplay-style smoothing; this is a planned cinematic move with authored timing.

### Rack focus
Animate focus distance or the focus object's relationship using the version-appropriate camera
settings. Verify the focus transition in rendered frames; a UI value alone is not proof of a
successful rack focus.

## 4. Animation and timing

1. Convert shot timecode to frames using the scene frame rate.
2. Place start and end keyframes explicitly.
3. Use the Graph Editor to shape ease-in/ease-out and avoid unintended overshoot.
4. Use linear interpolation only when constant speed is intentional.
5. Keep the camera stable during information-dense mechanism demonstrations.
6. Add a short arrival hold where the viewer needs to inspect a newly revealed detail.
7. Check the first, middle, and final frames, then play the entire move.
8. If the shot duration changes, update keyframes and verify the move still lands on the intended
   final frame.

For a moving camera, animate both camera position and aim target as a coordinated system. Avoid
Euler rotation flips; use a stable rig or quaternion-based orientation when needed.

## 5. Lighting and camera interaction

- Confirm the key light does not create glare over labels or transparent cutaway surfaces.
- Use rim light to separate the silhouette, not to outline every edge unnaturally.
- Keep exposure and white balance consistent with adjacent shots unless a deliberate transition
  is intended.
- Depth of field must not blur the part needed to understand the mechanism.
- Transparent materials often need simplified lighting and controlled reflections to remain
  readable.

## 6. Preview and render gates

Before final render:
- set final aspect ratio and resolution
- set frame range exactly to the shot
- check active camera
- inspect subject framing at first/mid/last frames
- inspect camera path for intersections and abrupt direction changes
- verify focus and depth of field
- check subtitle/graphic safe area
- compare the shot against previous/next approved shots
- render a low-cost preview and review it visually

Do not report success from a saved .blend file alone. Open or render it and inspect the output.
Keep preview and final render settings clearly distinguished.

## 7. Deliverable organization

Suggested per-project structure:

```text
project/
  shots/
    S01/
      shot-card.md
      scene/
        S01.blend
      preview/
        S01_preview.mp4
        contact-sheet.jpg
      final/
        S01_final.mp4
  assets/
  references/
  manifests/
    shot-continuity.md
```

Only claim files exist after confirming their paths and contents. Keep the .blend source and rendered
media linked to the shot ID.
