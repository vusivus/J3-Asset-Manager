# J3 Asset Manager Windows EXE distribution

Double-click `J3 Asset Manager.exe` to start the editor. The main application JAR is embedded in the EXE. Keep the EXE and `libraries` folder together.

This launcher uses an installed 64-bit Java 21 or newer. It checks `JAVA_HOME`, Windows Java registrations, and `PATH`, skipping older installations. It does not bundle a Java runtime. It unpacks the embedded application JAR to the Windows temp directory when launched. If no suitable Java installation is found, it displays an error with the required version.

The blue monkey and cube icon is embedded in the EXE. A separate `.ico` copy is included for packaging and shortcuts.
