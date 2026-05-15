# AR/VR Development — Anti-Patterns

Push back when you see these. Each one ships with a concrete fix path.

### Reading-heavy UI floating in space without anchors.

**Fix:** Anchor text to a stable surface (wrist, world space, controller). Cap reading content at one paragraph per panel. Use larger type than 2D defaults — 24pt minimum at 1m distance.

### Camera-coupled UI that induces sickness.

**Fix:** Decouple UI from head movement. Place HUD elements in world space at a comfortable distance (0.5–1m), not glued to the camera. Add a vignette during locomotion. Test with users new to VR.

### Fixed 'forward' assumed; no recenter affordance.

**Fix:** Add a recenter gesture (long-press menu button on Quest, double-tap crown on Vision Pro). Surface it in onboarding. Default to 'sitting' mode unless the experience requires 'standing' + room-scale.

### Hand-only input without controller fallback.

**Fix:** Detect hand-tracking quality. When confidence drops or the user picks up a controller, switch input modality without losing state. Test by occluding hands mid-interaction.

### Ignoring passthrough boundary in mixed reality.

**Fix:** Render the platform-defined boundary cue when the user approaches the play area edge. Pause gameplay or surface a warning before they hit a wall.


## How to push back

State the anti-pattern, name the specific evidence you saw, propose the minimal change, link the
official doc that justifies it. Don't moralize. Don't list every problem at once. One issue at a
time, confirm, move to the next.
