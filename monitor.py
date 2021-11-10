import psutil
import datetime





class checker:

    def critical_level(self):
        battery_threshold=65
        memory_threshold=30 #percentage
        context_switch_threshold=1455055


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
        #cached_memory=mem.cached
        #checking the logged in user
        user=psutil.users()
        username=user[0].name
        terminal_name=user[0].terminal
        #####CPU used 
        cpu=psutil.cpu_times()

        time_spent_system=cpu.system
        time_spent_idle=cpu.idle
        cpu=psutil.cpu_stats()
        cpu_inturrupts=cpu.interrupts
        context_switches=cpu.ctx_switches

        process_running=len(psutil.pids())


        return {
                "Time pushed":current_time,
                "user logged in":username,
                "Terminal used by user":terminal_name,
                "battery left in percentage":battery_left,
                "time left for server":time_remining,
                "is Pulgged to power":power_pugged,
                "percent ram used":precent_used,
                "free ram in kb":ram_free,
                "time spent on system process in seconds":time_spent_system,
                "time spent on idle process in seconds":time_spent_idle,
                "Total number of cpu intrrupts in cpu":cpu_inturrupts,
                "Context switches in the cpu":context_switches,
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
    def Ram_usage(self):
        current_time = datetime.datetime.now()

        mem=psutil.virtual_memory()
        precent_used=mem.percent
        ram_free=mem.free
        return {
            "Time pushed":current_time,
            "percent ram used":precent_used,
            "free ram in kb":ram_free,
        }

    def cpu_usage(self):
        current_time = datetime.datetime.now()

        cpu=psutil.cpu_times()

        time_spent_system=cpu.system
        time_spent_idle=cpu.idle
        cpu=psutil.cpu_stats()
        cpu_inturrupts=cpu.interrupts
        context_switches=cpu.ctx_switches

        return {
            "Time pushed":current_time,
            "time spent on system process in seconds":time_spent_system,
            "time spent on idle process in seconds":time_spent_idle,
            "Total number of cpu intrrupts in cpu":cpu_inturrupts,
            "Context switches in the cpu":context_switches,
        }
#print(checker().Status())
#"cached to the memory":cached_memory,