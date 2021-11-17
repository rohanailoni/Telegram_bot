import psutil
import datetime





class checker:

    


    def Status(self):
        current_time = datetime.datetime.now()
        #cecking battery
        bat=psutil.sensors_battery()
        battery_left=bat.percent
        time_remining=bat.secsleft
        power_pugged=bat.power_plugged
        #checking memory
        mem=psutil.virtual_memory()
        precent_used=mem.percent
        ram_free=mem.free


        process_running=len(psutil.pids())


        return {
                "Time pushed":current_time,
                "battery left in percentage":battery_left,
                "time left for server":time_remining,
                "is Pulgged to power":power_pugged,
                "percent ram used":precent_used,
                "free ram in kb":ram_free,
                "Number of process running in the cpu":process_running,
                }
    def Battery(self):
        current_time = datetime.datetime.now()

        bat=psutil.sensors_battery()
        battery_left=bat.percent
        time_remining=bat.secsleft
        power_pugged=bat.power_plugged

        return {
            "Time pushed":current_time,
            "battery left in percentage":battery_left,
                "time left for server":time_remining,
                "is Pulgged to power":power_pugged,
                
        }
    
        
#print(checker().Status())
#"cached to the memory":cached_memory,