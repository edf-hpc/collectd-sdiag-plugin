import collectd
import pyslurm

def read():
# Get sdiag stats

    stats = {}

    try:
        sdiag = pyslurm.statistics().get()
    except:
        return
    else:
        # Slurmctld Stats
        stats["server_thread_count"] = sdiag.get("server_thread_count")
        stats["agent_queue_size"] = sdiag.get("agent_queue_size")

        # Jobs Stats
        stats["jobs_submitted"] = sdiag.get("jobs_submitted")
        stats["jobs_started"] = sdiag.get("jobs_started")
        stats["jobs_completed"] = sdiag.get("jobs_completed")
        stats["jobs_canceled"] = sdiag.get("jobs_canceled")
        stats["jobs_failed"] = sdiag.get("jobs_failed")

        # Main Scheduler Stats
        stats["main_last_cycle"] = sdiag.get("schedule_cycle_last")
        stats["main_max_cycle"] = sdiag.get("schedule_cycle_max")
        stats["main_total_cycles"] = sdiag.get("schedule_cycle_counter")

        if sdiag.get("schedule_cycle_counter") > 0:
            stats["main_mean_cycle"] = (
                sdiag.get("schedule_cycle_sum") / sdiag.get("schedule_cycle_counter")
            )
            stats["main_mean_depth_cycle"] = (
                sdiag.get("schedule_cycle_depth") / sdiag.get("schedule_cycle_counter")
            )

        if (sdiag.get("req_time") - sdiag.get("req_time_start")) > 60:
            stats["main_cycles_per_minute"] = (
                sdiag.get("schedule_cycle_counter") /
                ((sdiag.get("req_time") - sdiag.get("req_time_start")) / 60)
            )

        stats["main_last_queue_length"] = sdiag.get("schedule_queue_len")

        # Backfilling stats
        stats["bf_total_jobs_since_slurm_start"] = sdiag.get("bf_backfilled_jobs")
        stats["bf_total_jobs_since_cycle_start"] = sdiag.get("bf_last_backfilled_jobs")
        stats["bf_total_cycles"] = sdiag.get("bf_cycle_counter")
        stats["bf_last_cycle"] = sdiag.get("bf_cycle_last")
        stats["bf_max_cycle"] = sdiag.get("bf_cycle_max")
        stats["bf_queue_length"] = sdiag.get("bf_queue_len")

        if sdiag.get("bf_cycle_counter") > 0:
            stats["bf_mean_cycle"] = (
                sdiag.get("bf_cycle_sum") / sdiag.get("bf_cycle_counter")
            )
            stats["bf_depth_mean"] = (
                sdiag.get("bf_depth_sum") / sdiag.get("bf_cycle_counter")
            )
            stats["bf_depth_mean_try"] = (
                sdiag.get("bf_depth_try_sum") / sdiag.get("bf_cycle_counter")
            )
            stats["bf_queue_length_mean"] = (
                sdiag.get("bf_queue_len_sum") / sdiag.get("bf_cycle_counter")
            )

	stats["bf_last_depth_cycle"] = sdiag.get("bf_last_depth")
	stats["bf_last_depth_cycle_try"] = sdiag.get("bf_last_depth_try")
	
	# Rpc per user stats
	for k, v in sdiag.get("rpc_user_stats").items():
		for h, u in v.items():
			if ( str(h) != 'id'):
				print k, "-->", h, "-->", u
				metric = str(k) + "-" + str(h)
				stats[metric] = u
	# RPC message stats
	for k, v in sdiag.get("rpc_type_stats").items():
                for h, u in v.items():
			if ( str(h) != 'id'):
                		print k, "-->", h, "-->", u
                        	metric = str(k) + "-" + str(h)
                        	stats[metric] = u		
	
	# Dispatch values to collectd
	for k , v in stats.items():
		print k, "-->", v
		v_tmp = collectd.Values(plugin='sdiag_stats', type="gauge",type_instance=k)
		v_tmp.dispatch(values=[v])
	
collectd.register_read(read)
