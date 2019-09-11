# (C) Datadog, Inc. 2019
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from datadog_checks.dev import get_here

HERE = get_here()

INSTANCE = {'ticket_location': 'foo'}

KAFKA_METRIC = {
    u'metric': u'mapr.process.context_switch_involuntary',
    u'value': 6308,
    u'tags': {
        u'clustername': u'demo',
        u'process_name': u'apiserver',
        u'clusterid': u'7616098736519857348',
        u'fqdn': u'mapr-lab-2-ghs6.c.datadog-integrations-lab.internal',
    },
}

DISTRIBUTION_METRIC = {
    "metric": "mapr.db.table.latency",
    "buckets": {"2,5": 21, "5,10": 11},
    "tags": {
        "table_fid": "2070.42.262546",
        "table_path": "/var/mapr/mapr.monitoring/tsdb-meta",
        "noindex": "//primary",
        "rpc_type": "put",
        "fqdn": "mapr-lab-2-dhk4.c.datadog-integrations-lab.internal",
        "clusterid": "7616098736519857348",
        "clustername": "demo",
    },
}

METRICS_IN_FIXTURE = {
    'mapr.cache.lookups_data',
    'mapr.cache.lookups_dir',
    'mapr.cache.lookups_inode',
    'mapr.cache.lookups_largefile',
    'mapr.cache.lookups_meta',
    'mapr.cache.lookups_smallfile',
    'mapr.cache.lookups_table',
    'mapr.cache.misses_data',
    'mapr.cache.misses_dir',
    'mapr.cache.misses_inode',
    'mapr.cache.misses_largefile',
    'mapr.cache.misses_meta',
    'mapr.cache.misses_smallfile',
    'mapr.cache.misses_table',
    'mapr.db.append_bytes',
    'mapr.db.append_rpcrows',
    'mapr.db.append_rpcs',
    'mapr.db.cdc.pending_bytes',
    'mapr.db.cdc.sent_bytes',
    'mapr.db.checkandput_bytes',
    'mapr.db.checkandput_rpcrows',
    'mapr.db.checkandput_rpcs',
    'mapr.db.flushes',
    'mapr.db.forceflushes',
    'mapr.db.fullcompacts',
    'mapr.db.get_bytes',
    'mapr.db.get_currpcs',
    'mapr.db.get_readrows',
    'mapr.db.get_resprows',
    'mapr.db.get_rpcs',
    'mapr.db.increment_bytes',
    'mapr.db.increment_rpcrows',
    'mapr.db.increment_rpcs',
    'mapr.db.index.pending_bytes',
    'mapr.db.minicompacts',
    'mapr.db.put_bytes',
    'mapr.db.put_currpcs',
    'mapr.db.put_readrows',
    'mapr.db.put_rpcrows',
    'mapr.db.put_rpcs',
    'mapr.db.repl.pending_bytes',
    'mapr.db.repl.sent_bytes',
    'mapr.db.scan_bytes',
    'mapr.db.scan_currpcs',
    'mapr.db.scan_readrows',
    'mapr.db.scan_resprows',
    'mapr.db.scan_rpcs',
    'mapr.db.ttlcompacts',
    'mapr.db.updateandget_bytes',
    'mapr.db.updateandget_rpcrows',
    'mapr.db.updateandget_rpcs',
    'mapr.db.valuecache_hits',
    'mapr.db.valuecache_lookups',
    'mapr.db.valuecache_usedSize',
    'mapr.fs.bulk_writes',
    'mapr.fs.bulk_writesbytes',
    'mapr.fs.kvstore_delete',
    'mapr.fs.kvstore_insert',
    'mapr.fs.kvstore_lookup',
    'mapr.fs.kvstore_scan',
    'mapr.fs.local_readbytes',
    'mapr.fs.local_reads',
    'mapr.fs.local_writebytes',
    'mapr.fs.local_writes',
    'mapr.fs.read_bytes',
    'mapr.fs.read_cachehits',
    'mapr.fs.read_cachemisses',
    'mapr.fs.reads',
    'mapr.fs.statstype_create',
    'mapr.fs.statstype_lookup',
    'mapr.fs.statstype_read',
    'mapr.fs.statstype_write',
    'mapr.fs.write_bytes',
    'mapr.fs.writes',
    'mapr.io.read_bytes',
    'mapr.io.reads',
    'mapr.io.write_bytes',
    'mapr.io.writes',
    'mapr.metrics.submitted',
    'mapr.process.context_switch_involuntary',
    'mapr.process.context_switch_voluntary',
    'mapr.process.cpu_percent',
    'mapr.process.cpu_time.syst',
    'mapr.process.cpu_time.user',
    'mapr.process.data',
    'mapr.process.disk_octets.read',
    'mapr.process.disk_octets.write',
    'mapr.process.disk_ops.read',
    'mapr.process.disk_ops.write',
    'mapr.process.mem_percent',
    'mapr.process.page_faults.majflt',
    'mapr.process.page_faults.minflt',
    'mapr.process.rss',
    'mapr.process.vm',
    'mapr.rpc.bytes_recd',
    'mapr.rpc.bytes_sent',
    'mapr.rpc.calls_recd',
    'mapr.streams.listen_bytes',
    'mapr.streams.listen_currpcs',
    'mapr.streams.listen_msgs',
    'mapr.streams.listen_rpcs',
    'mapr.streams.produce_bytes',
    'mapr.streams.produce_msgs',
    'mapr.streams.produce_rpcs',
}


STREAM_ID_FIXTURE = {
    ('dapilufuco61', 1): 0,
    ('dapilufuco61', 2): 0,
    ('dapilufuco61', 3): 1,
    ('dapilufuco61', 4): 0,
    ('dapilufuco61', 5): 0,
    ('dapilufuco61', 6): 4,
    ('dapilufuco61', 7): 1,
    ('dapilufuco61', 8): 0,
    ('dapilufuco61', 9): 4,
    ('giwanoyoki81', 1): 0,
    ('giwanoyoki81', 2): 1,
    ('giwanoyoki81', 3): 1,
    ('giwanoyoki81', 4): 3,
    ('giwanoyoki81', 5): 0,
    ('giwanoyoki81', 6): 1,
    ('giwanoyoki81', 7): 0,
    ('giwanoyoki81', 8): 7,
    ('giwanoyoki81', 9): 7,
    ('juzisumoya51', 1): 0,
    ('juzisumoya51', 2): 1,
    ('juzisumoya51', 3): 1,
    ('juzisumoya51', 4): 3,
    ('juzisumoya51', 5): 1,
    ('juzisumoya51', 6): 1,
    ('juzisumoya51', 7): 3,
    ('juzisumoya51', 8): 3,
    ('juzisumoya51', 9): 7,
    ('ligokiboda25', 1): 0,
    ('ligokiboda25', 2): 1,
    ('ligokiboda25', 3): 2,
    ('ligokiboda25', 4): 1,
    ('ligokiboda25', 5): 2,
    ('ligokiboda25', 6): 5,
    ('ligokiboda25', 7): 2,
    ('ligokiboda25', 8): 1,
    ('ligokiboda25', 9): 2,
    ('linidojajo26', 1): 0,
    ('linidojajo26', 2): 0,
    ('linidojajo26', 3): 0,
    ('linidojajo26', 4): 0,
    ('linidojajo26', 5): 1,
    ('linidojajo26', 6): 0,
    ('linidojajo26', 7): 3,
    ('linidojajo26', 8): 0,
    ('linidojajo26', 9): 3,
    ('nuwahibicu11', 1): 0,
    ('nuwahibicu11', 2): 0,
    ('nuwahibicu11', 3): 1,
    ('nuwahibicu11', 4): 2,
    ('nuwahibicu11', 5): 2,
    ('nuwahibicu11', 6): 4,
    ('nuwahibicu11', 7): 5,
    ('nuwahibicu11', 8): 6,
    ('nuwahibicu11', 9): 1,
    ('pafuvonuki94', 1): 0,
    ('pafuvonuki94', 2): 0,
    ('pafuvonuki94', 3): 1,
    ('pafuvonuki94', 4): 2,
    ('pafuvonuki94', 5): 0,
    ('pafuvonuki94', 6): 4,
    ('pafuvonuki94', 7): 2,
    ('pafuvonuki94', 8): 2,
    ('pafuvonuki94', 9): 7,
    ('rigugepihi22', 1): 0,
    ('rigugepihi22', 2): 0,
    ('rigugepihi22', 3): 2,
    ('rigugepihi22', 4): 2,
    ('rigugepihi22', 5): 4,
    ('rigugepihi22', 6): 2,
    ('rigugepihi22', 7): 5,
    ('rigugepihi22', 8): 6,
    ('rigugepihi22', 9): 8,
    ('wutetusaba14', 1): 0,
    ('wutetusaba14', 2): 1,
    ('wutetusaba14', 3): 1,
    ('wutetusaba14', 4): 3,
    ('wutetusaba14', 5): 1,
    ('wutetusaba14', 6): 1,
    ('wutetusaba14', 7): 5,
    ('wutetusaba14', 8): 7,
    ('wutetusaba14', 9): 4,
    ('yufidaxare27', 1): 0,
    ('yufidaxare27', 2): 0,
    ('yufidaxare27', 3): 1,
    ('yufidaxare27', 4): 0,
    ('yufidaxare27', 5): 4,
    ('yufidaxare27', 6): 4,
    ('yufidaxare27', 7): 6,
    ('yufidaxare27', 8): 0,
    ('yufidaxare27', 9): 4,
}