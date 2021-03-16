CREATE TABLE IF NOT EXISTS resto.inspection (
	idrestaurant int,
	inspectiondate date,
	criticalflag text,
	grade text,
	score int,
	violationcode text,
	violationdescription text,
	PRIMARY KEY (idrestaurant, inspectiondate))
	WITH ID = c865a110-863e-11eb-a216-df5483c2a0ca
	AND CLUSTERING ORDER BY (inspectiondate ASC)
	AND bloom_filter_fp_chance = 0.01
	AND dclocal_read_repair_chance = 0.1
	AND crc_check_chance = 1.0
	AND default_time_to_live = 0
	AND gc_grace_seconds = 864000
	AND min_index_interval = 128
	AND max_index_interval = 2048
	AND memtable_flush_period_in_ms = 0
	AND read_repair_chance = 0.0
	AND speculative_retry = '99PERCENTILE'
	AND comment = ''
	AND caching = { 'keys': 'ALL', 'rows_per_partition': 'NONE' }
	AND compaction = { 'max_threshold': '32', 'min_threshold': '4', 'class': 'org.apache.cassandra.db.compaction.SizeTieredCompactionStrategy' }
	AND compression = { 'chunk_length_in_kb': '64', 'class': 'org.apache.cassandra.io.compress.LZ4Compressor' }
	AND cdc = false
	AND extensions = {  };
CREATE INDEX IF NOT EXISTS index_grade ON resto.inspection (grade);
