# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('Images', 'Trabalho\\Images'), ('rep_musicas', 'Trabalho\\rep_musicas'), ('__pycache__', 'Trabalho\\__pycache__')],
    hiddenimports=['PySimpleGUI', 
        'pygame', 
        'pygame.mixer',
        'pygame.locals',
        'pygame.font',
        'pygame.event'
        'os'
        'time'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
