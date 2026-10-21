$ErrorActionPreference = 'Stop'

$packageDirectory = 'C:\Users\VTStudios\AppData\Roaming\Blender Foundation\Blender\5.2\scripts\addons\pathix'
$packageInit = Join-Path $packageDirectory '__init__.py'
$sourceModule = Join-Path $PSScriptRoot 'pathix_jme_export.py'
$targetModule = Join-Path $packageDirectory 'pathix_jme_export.py'

if (-not (Test-Path -LiteralPath $packageInit)) {
    throw "Pathix addon was not found at $packageInit"
}
if (-not (Test-Path -LiteralPath $sourceModule)) {
    throw "Export module was not found at $sourceModule"
}

$original = [System.IO.File]::ReadAllText($packageInit)
$updated = $original
function Add-AfterAnchor([string]$anchor, [string]$addition) {
    if ($script:updated.Contains($addition)) { return }
    if (-not $script:updated.Contains($anchor)) {
        throw "Pathix source changed; missing patch anchor: $anchor"
    }
    $script:updated = $script:updated.Replace($anchor, $anchor + "`n" + $addition)
}

Add-AfterAnchor 'import os' 'from . import pathix_jme_export'
Add-AfterAnchor "            op = box_41794.operator('object.editmode_toggle', text='edit mode', icon_value=0, emboss=True, depress=(bpy.context.mode == 'EDIT_MESH'))" "            box_41794.operator('pathix.export_jme_glb', text='Export GLB for jME3', icon='EXPORT')"
Add-AfterAnchor '    bpy.utils.register_class(SNA_OT_Convert_13213)' '    pathix_jme_export.register()'
if (-not $updated.Contains('    pathix_jme_export.unregister()')) {
    $anchor = '    bpy.utils.unregister_class(SNA_OT_Convert_13213)'
    if (-not $updated.Contains($anchor)) { throw "Pathix source changed; missing patch anchor: $anchor" }
    $updated = $updated.Replace($anchor, '    pathix_jme_export.unregister()' + "`n" + $anchor)
}
$updated = $updated.Replace('"version" : (1, 1, 0)', '"version" : (1, 1, 2)')
$updated = $updated.Replace('"version" : (1, 1, 1)', '"version" : (1, 1, 2)')

$stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
Copy-Item -LiteralPath $packageInit -Destination "$packageInit.$stamp.bak"
if (Test-Path -LiteralPath $targetModule) {
    Copy-Item -LiteralPath $targetModule -Destination "$targetModule.$stamp.bak"
}
[System.IO.File]::WriteAllText($packageInit, $updated, [System.Text.UTF8Encoding]::new($false))
Copy-Item -LiteralPath $sourceModule -Destination $targetModule -Force
Write-Output "Installed Pathix GLB exporter. Backup: $packageInit.$stamp.bak"
