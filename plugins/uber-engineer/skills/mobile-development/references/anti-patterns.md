# Mobile Development — Anti-Patterns

Push back when you see these. Each one ships with a concrete fix path.

### Web layouts copy-pasted into mobile without redesign for thumb reach.

**Fix:** Move primary actions into the bottom 30% of the screen. Replace hover affordances with long-press or a visible button. Verify thumb reach at iPhone SE width and Pro Max width.

### Permissions requested on launch instead of in context.

**Fix:** Defer permission prompts until the user attempts the action that requires them (camera prompt when they tap the camera icon, location prompt when they open the map). Pre-prompt screen explains why before the OS dialog.

### Treating the simulator as 'tested' — never run on a physical device with real network.

**Fix:** Add a 'physical device pass' to the release checklist. Test on cellular (LTE + 5G), low battery mode, and at least one device two generations old.

### Push tokens not refreshed; users silently lose notifications after token rotation.

**Fix:** Implement the platform refresh callback (didRegisterForRemoteNotificationsWithDeviceToken on iOS, onNewToken on Android). Sync the new token to your backend on app launch and on rotation. Verify by uninstalling + reinstalling and confirming pushes resume.

### Hardcoded API URLs that ship to TestFlight and prod alike.

**Fix:** Move the base URL into a build configuration that varies per scheme/variant (Debug, Beta, Release). Verify TestFlight builds hit staging, App Store builds hit prod, and no environment leaks across.


## How to push back

State the anti-pattern, name the specific evidence you saw, propose the minimal change, link the
official doc that justifies it. Don't moralize. Don't list every problem at once. One issue at a
time, confirm, move to the next.
