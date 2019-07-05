import pythonmatsim.jvm as jvm

jvm.start_jvm()

import javawrappers.org.matsim.core.config as jconfig
import javawrappers.java.net as jnet
import javawrappers.org.matsim.core.controler as jcontroler

from pythonmatsim.api.events import *
import events_pb2 as events
from typing import Union

import tempfile

# This line is not strictly necessary, but helps IDEs identify that file as "executable"
if __name__ == "__main__":
    # Do everything in a temporary directory that will be deleted at the end. Not always the best choice,
    # but good idea when doing interactive analysis
    with tempfile.TemporaryDirectory() as tmp:
        # in PyCharm, such chains are possible with autocomplete all the way, with type hints for the parameters
        # This unfortunately does not work in Jupyter.
        config = jconfig.ConfigUtils.loadConfig(jnet.URL('https://raw.githubusercontent.com/matsim-org/matsim/master/examples/scenarios/equil/config.xml'))

        config.controler().setDumpDataAtEnd(False)
        config.controler().setLastIteration(1)

        config.controler().setOutputDirectory(tmp)

        controler = jcontroler.Controler(config)

        class ShoutListener(EventListener):
            def reset(self, iteration):
                print("########################################################################################")
                print(iteration)

            @listen_to(EventType.actStart, EventType.actEnd)
            def handleAct(self, event: Union[events.ActivityStartEvent, events.ActivityEndEvent]):
                # Somehow type hint above does not help. Need to investigate
                print(event.persId)

        add_event_handler(controler, ShoutListener())
        controler.run()

