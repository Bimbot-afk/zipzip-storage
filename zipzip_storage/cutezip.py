def colors(color):

    palette = {
        "RESET": "\033[0m",
        "BOLD": "\033[1m",
        "RED": "\033[31m",
        "GREEN": "\033[32m",
        "YELLOW": "\033[33m",
        "CYAN": "\033[36m"
    }

    return palette.get(color.upper(), "")


def print_zipzipzip(path):
    print(colors("GREEN") + """

               .dMMMMMMMMMMMMMMMMMMMMMMb.
            .dMMMMMMMMMMMMMMMMMMMMMMMMMMMMb.
          .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.
         dMMMMMMMP'        ``YMMMMMMM       `YMMb
        dMMMMMMM'             `MMMMMM'         `MMb
       dMMMMMMM'               `MMMM'           `MMb
       MMMMMMMM                 MMMM             MMM
       MMMMMMMM                 MMMM             MMM
       MMMMMMMMb               dMMMM            dMM'
       YMMMMMMMMb             dMMMMMb          dMM'
        YMMMMMMMMMb.       .dMMMMMMMMMb.      dMMP
         `YMMMMMMMMMMMbbMMMMMMMMMMMMMMMMMbb.dMMP'
           `YMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMP'
             `YMMMMMMMMMMMMMMMMMMMMMMMMMMMMP'
                `TMMMMMMMMMMMMMMMMMMMMMMMP'
                   `TMMMMMMMMMMMMMMMMP'
                        |MMMMMMM|
                        |MMMMMMM|
                        |MMMMMMM|
                       dMMMMMMMMMb
                     .MMMMMMMMMMMMM.
                   .MMMMMMMMMMMMMMMMM.
    """)
    print(f"Current Folder: {path}")