"""Parse WestburyLab UsenetCorpus into JSON objects

    Can download from:
    http://www.psych.ualberta.ca/~westburylab/downloads/usenetcorpus.download.html

    12GB Compressed - UsenetCorpus.txt.tar.gz
    37GB Uncompressed - WestburyLab.NonRedundant.UsenetCorpus.txt
    35.7GB @ 32,880,805 JSON Objects

"""

import re
import json

bigfile = open("WestburyLab.NonRedundant.UsenetCorpus.txt", "rb")


def main(file_on_disk):
    """Read in each line of file until END.OF.DOCUMENT is found,
        write to JSON, print number of objects"""

    counter = 0
    object_gen = ""

    for line in file_on_disk:
        if not re.match("(.*)---END.OF.DOCUMENT---(.*)", str(line)):
            if len(line.rstrip()) > 2:
                decode_line = line.decode("utf-8", "ignore").rstrip()
                object_gen = object_gen + decode_line
        else:

            j = {'post': object_gen}
            # now write output to a file
            write_json(j)
            object_gen = ""
            counter += 1
            print(counter)


def write_json(d_object):
    """Append dict to file as JSON object"""

    with open("data.json", "a") as json_file:
        json_file.write(json.dumps(d_object, indent=4, sort_keys=True))
        json_file.close()

if __name__ == "__main__":
    main(bigfile)
