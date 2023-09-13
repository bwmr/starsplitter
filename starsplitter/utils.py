def return_session(str):
    """
    Warp Session generated from rlnImageName based on the following assumed path:

    $warp_folder/subtomo/$tomo/$tomo_$nr_$angpix.mrc
    """
    return str.split("/")[-4]