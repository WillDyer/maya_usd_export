import traceback, importlib
if __name__ == "__main__":
    from . import export_usd
else:
    try:
        import export_usd
    except:
        traceback.print_exc()
        exit()
importlib.reload(export_usd)


def export(output=None, debug=False, start_frame=None, end_frame=None):
    if not output:
        output = "/run/media/will/Will_s SSD1/University_Projects/YR3/Boar/export/"
    export_usd.ExportAnim(
        geo_whitelist=["render", "muscle", "bone"],
        usd_type="Xform",
        root_type="SkelRoot",
        output=output,
        debug=debug,
        export_rig=True,
        start_frame=start_frame,
        end_frame=end_frame,
    )
