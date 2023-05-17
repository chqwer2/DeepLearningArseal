import sys
sys.path.append("video_features")




from pathlib import Path

def build_cfg_path(feature_type: str) -> os.PathLike:
    '''Makes a path to the default config file for each feature family.

    Args:
        feature_type (str): the type (e.g. 'vggish')

    Returns:
        os.PathLike: the path to the default config for the type
    '''
    path_base = Path('./video_features/configs')
    path = path_base / f'{feature_type}.yml'
    return path
