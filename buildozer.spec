      - name: Build with Buildozer
        run: |
          export PATH=$PATH:$HOME/.local/bin
          # 1. Pre-accept licenses by creating the license files manually
          mkdir -p "$ANDROID_HOME/licenses" || true
          echo "24333f8a63b682569cc481586c2aa69473b61310" > "$ANDROID_HOME/licenses/android-sdk-license"
          echo "84831b9409646a918e30573bab4c9c91346d8abd" > "$ANDROID_HOME/licenses/android-sdk-preview-license"
          
          # 2. Force Buildozer to run in non-interactive mode
          # We use 'yes' again as a secondary fail-safe
          yes | buildozer -v android debug
        env:
          BUILDOZER_ALLOW_ORG_NAME_AS_PACKAGE_NAME: 1
          # Anchor the SDK/NDK path for the runner
          ANDROID_HOME: /usr/local/lib/android/sdk
          APP_ANDROID_ACCEPT_SDK_LICENSE: 1
          
