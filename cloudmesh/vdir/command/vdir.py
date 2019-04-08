from __future__ import print_function

from cloudmesh.common.console import Console
from cloudmesh.shell.command import PluginCommand
from cloudmesh.shell.command import command
from cloudmesh.vdir.api.manager import Vdir


class VdirCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_vdir(self, args, arguments):
        """
        ::

          Usage:
                vdir mkdir DIR
                vdir cd [DIR]
                vdir ls [DIR]
                vdir add [FILEENDPOINT] [DIR_AND_NAME]
                vdir delete [DIR_OR_NAME]
                vdir status [DIR_OR_NAME]
                vdir get NAME

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file

          Descripton:

              A virtual directory is explained in our NIST doecumentation. It
              contains a number of links that point to other storage services on
              which the file is stored. The links include the provider, the name
              of the profider and its type are identified in the
              ~/.cloudmesh4.yaml file.

              the location is identified as

                 {provider}:{directory}/{filensme}

              A cloudmesh directory can be used to uniquely specify the file:

                 cm:
                    name: the unique name of the file
                    kind: vdir
                    cloud: local
                    directory: directory
                    filename: filename
                    directory: directory
                    provider: provider
                    created: date
                    modified: date

              vdir get NAME

                 locates the file with the name on a storage provider,
                 and fetches it from there.


        """

        print(arguments)

        d = Vdir()

        Console.error("This is just a sample")
        return ""

