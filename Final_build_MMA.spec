# -*- mode: python -*-

block_cipher = None


a = Analysis(['Final_build_MMA.py'],
             pathex=['C:\\Users\\ajith\\Desktop\\Python\\MouseMotionApplication'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Final_build_MMA',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
