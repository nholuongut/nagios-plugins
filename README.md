# Advanced Nagios Plugins Collection

![](https://i.imgur.com/waxVImv.png)
### [View all Roadmaps](https://github.com/nholuongut/all-roadmaps) &nbsp;&middot;&nbsp; [Best Practices](https://github.com/nholuongut/all-roadmaps/blob/main/public/best-practices/) &nbsp;&middot;&nbsp; [Questions](https://www.linkedin.com/in/nholuong/)
<br/>

**Largest, most advanced collection of production-grade Nagios monitoring code (over 450 programs)**

Specialised plugins for AWS, Hadoop, Big Data & NoSQL technologies, written by a former Clouderan ([Cloudera](http://www.cloudera.com) was the first Hadoop Big Data vendor) and ex-[Hortonworks](http://www.hortonworks.com) consultant.

Supports most major open source NoSQL technologies, Pub-Sub / Message Buses, CI, Web and Linux based infrastructure, including:

- [AWS](https://aws.amazon.com/)
- [Hadoop](http://hadoop.apache.org/) - extensive API integration to all major Hadoop vendors ([Cloudera](http://www.cloudera.com), [Hortonworks](http://www.hortonworks.com), [MapR](http://www.mapr.com), [IBM BigInsights](https://www.ibm.com/support/knowledgecenter/SSPT3X_4.0.0/com.ibm.swg.im.infosphere.biginsights.product.doc/doc/c0057605.html))
- [Docker](https://www.docker.com/)
- [Kafka](http://kafka.apache.org/)
- [RabbitMQ](http://www.rabbitmq.com/)
- [Elasticsearch](https://www.elastic.co/products/elasticsearch)
- [Solr / SolrCloud](http://lucene.apache.org/solr/)
- [HBase](https://hbase.apache.org/)
- [Cassandra](http://cassandra.apache.org/)
- [Redis](http://redis.io/)
- [CouchDB](http://couchdb.apache.org/)
- [Consul](https://www.consul.io/)
- [ZooKeeper](https://zookeeper.apache.org/)
- [Jenkins](https://jenkins.io/)
- [Travis CI](https://travis-ci.org/)
- [Puppet](https://puppet.com/)
- Linux - various including the widely used `check_yum.py` for [RHEL](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux) / [CentOS](https://www.centos.org/) yum security updates
- SSL Certificate expiry in days & validations
- Whois domain expiry in days & validations
- advanced DNS record checks (MX, NS, SRV etc)
- [Git](https://git-scm.com/), [MySQL](https://www.mysql.com/) ... etc.

Supports a a wide variety of [compatible Enterprise Monitoring systems](nholuongut/nagios-nholuongut/nagios-pluginsing-systems).

Most enterprise monitoring systems come with basic generic checks, while this project extends their monitoring capabilities significantly further in to advanced infrastructure, application layer, APIs etc.

If running against services in Cloud or Kubernetes, just target the load balancer address or the Kubernetes Service or Ingress addresses.

Also useful to be run on the command line for testing or in scripts for dependency availability checking, and comes with a selection of [advanced HAProxy configurations](https://github.com/nholuongut/HAProxy-configs) for these technologies to make monitoring and scripting easier for clustered technologies.

Fix requests, suggestions, updates and improvements are most welcome via Github [issues](nholuongut/nagios-nholuongut/nagios-pluginsequests](nholuongut/nagios-plugins/pulls) (in wnholuongut/nagios-pluginse you credit and mark you as a contributor to the project :) ).

**Make sure you run `make update` if updating and not just `git pull` as you will often need the latest library submodules and probably new upstream libraries too**

## Quick Start

1. Git clone this repo and compile dependencies by running `make`<br>
      OR<br>
1. Download pre-built self-contained [Docker image](https://hub.docker.com/r/nholuongut/nagios-plugins/)

Execute each program on the command line with `--help` to see its options.

### Ready-to-run Docker Image

All plugins and their pre-compiled dependencies can be found ready-to-run on [DockerHub](https://hub.docker.com/r/nholuongut/nagios-plugins/), if you have [Docker](https://www.docker.com/) installed, fetch this project like so:

```shell
docker pull nholuongut/nagios-plugins
```

List all plugins:

```shell
docker run nholuongut/nagios-plugins
```

Run any given plugin by suffixing it to the `docker run` command:

```shell
docker run nholuongut/nagios-plugins <program> <args>
```

eg.

```shell
docker run nholuongut/nagios-plugins check_ssl_cert.pl --help
```

There are also `:centos` (`:latest`), `:alpine`, `:debian`, `:fedora` and `:ubuntu` tagged docker images available, as well as `:python` and `:perl` only images.

You should tag the build locally as `:stable` or date-time stamped and run off that tag to avoid it getting auto-replaced by newer `:latest` builds, to control updates to suit your schedule and prevent random delays from `docker run`s pulling down newer builds from DockerHub.

### Automated Build from Source

```shell
curl -L https://git.io/nagios-plugins-bootstrap | sh
```

or

```shell

git clone nholuongut/nagios-nholuongut/nagios-plugins

cd nagios-plugins

make

```

Now run any plugin with `--help` to find out which switches to use.

Make sure to read [Detailed Build Instructions](nholuongut/nagios-nholuongut/nagios-pluginstructions) further down for more information.

#### Optional: Generate self-contained Perl scripts with all dependencies built in to each file for easy distribution

After the `make` build has finished, if you want to make self-contained versions of all the perl scripts with all dependencies included for copying around, run:

```shell
make fatpacks
```

The self-contained scripts will be available in the `fatpacks/` directory.

## Quick Plugins Guide

There are over 400 programs in this repo so these are just some of the highlights.

### Quick Links

- [Hadoop Ecosystem](nholuongut/nagios-nholuongut/nagios-plugins- HDFS, Yarn, HBase, Ambari, Atlas, Ranger
  - [Hadoop Distributions](nholuongut/nagios-nholuongut/nagios-pluginsns) - Cloudera, Hortonworks, MapR, IBM BigInsights
  - [SQL-on-Hadoop](nholuongut/nagios-nholuongut/nagios-pluginsive, Drill, Presto
- [Service Discovery & Coordination](nholuongut/nagios-nholuongut/nagios-plugins-coordination) - ZooKeeper, Consul, Vault
- [Cloud](nholuongut/nagios-nholuongut/nagios-plugins
- [Docker / Containerization](nholuongut/nagios-nholuongut/nagios-pluginszation) - Docker & Docker Swarm, Mesos, Kubernetes
- [Search](nholuongut/nagios-nholuongut/nagios-pluginsearch, Solr / SolrCloud
- [NoSQL](nholuongut/nagios-nholuongut/nagios-plugins, Redis, Riak, Memcached, CouchDB
- [SQL Databases](nholuongut/nagios-nholuongut/nagios-pluginsySQL
- [Pub-Sub / Message Queues](nholuongut/nagios-nholuongut/nagios-pluginse--message-queues) - Kafka, Redis, RabbitMQ
- [CI - Continuous Integration & Build Systems](nholuongut/nagios-nholuongut/nagios-pluginstegration--build-systems---git-jenkins-travis-ci--dockerhub-automated-builds) - Jenkins, Travis CI, GoCD, DockerHub, Git
- [Infrastructure](nholuongut/nagios-nholuongut/nagios-pluginsnternet---web-dns-ssl-domains)
  - [Internet](nholuongut/nagios-nholuongut/nagios-pluginsnternet---web-dns-ssl-domains) - Web, DNS, SSL & Domain Expiry
  - [Linux](nholuongut/nagios-nholuongut/nagios-pluginsinux---os-network-puppet-raid-ssh-clusters-yum-security-updates) - OS, Network, Puppet, RAID, SSH, Clusters, Yum Security Updates

#### Hadoop Ecosystem

- `check_hadoop_*.pl/py` - various [Apache Hadoop](http://hadoop.apache.org/) monitoring utilities for HDFS, YARN and MapReduce (both MRv1 & MRv2):
  - Hadoop - Masters' status and High Availability (ZKFC, Active/Standby state), Worker nodes counts, dead nodes / blacklisted / unhealthy nodes, heap usage, metrics and JMX information with optional thresholds & graph data
  - HDFS - NameNode & DataNode checks, cluster space, balance, block replication, block count limits per datanode / cluster total, safe mode, failed name dirs, WebHDFS (with HDFS HA failover support), HttpFS, HDFS writeability, rack resilience configuration (checks more than 1 rack configured, finds nodes with default rack configured), HDFS fsck status / last check / run time / max blocks, HDFS file / directory existence & metadata attributes
  - Yarn:
    - Infrastructure - Resource Manager and NodeManager checks, unhealthy NodeManagers, queue state, queue capacity, app stats, % of memory allocated, metrics with optional thresholds to check things such as activeNodes, appsPending, lostNodes, unhealthyNodes etc.
    - Apps - app last finished state / user / queue / elapsed time (batch job SLAs), queue apps allowed/disallowed (catch Spark Shells on production queue), app running (check long living yarn service is still alive), long running apps/jobs detection with name and queue include/exclude regexes (detect SLAs breaches for in-progress batch jobs or forgotten Spark Shells holding resources, both Spark Scala and PySpark)
- `check_hbase_*.py/pl` - various [Apache HBase](https://hbase.apache.org/) monitoring utilities using Thrift + Stargate APIs, checks Masters / Backup Masters, RegionServers, table availability (exists, is enabled, and has minimum number of column families), number of expected table regions, unassigned table regions, regions stuck in transition, region count balance across RegionServers, requests per sec balance across RegionServers, compaction in progress (by table and by regionserver), number of regions in transition, longest current region migration time, hbck status for any inconsistencies, cell content vs optional regex + thresholds, table write and read back of unique generated values with write/read/delete latency checks against all detected column families, table write spray and read back of unique values across all regions for all column families with write/read/delete latency checks, gather metrics
- `check_atlas_*.py` - [Apache Atlas](http://atlas.apache.org/) metadata server instance status, as well as metadata entity checks including entity existence, state=ACTIVE, expected type, expected tags are assigned to entity (eg. PII - important because Ranger ACLs to allow or deny access to data can be assigned based on tags)
- `check_ranger_*.pl/.py` - [Apache Ranger](https://ranger.apache.org/) checks:
  - policy checks - existence, enabled, has auditing enabled, is recursive, last updated vs thresholds (to catch changes), repository name and type that the policy belongs to
  - repository checks - existence, active, type (eg. hive, hdfs), last updated vs thresholds (to catch changes)
  - number of policies and repositories vs thresholds
- `check_ambari_*.pl` - [Apache Ambari](https://ambari.apache.org/) API checks for Hadoop clusters written running the standard open source [Hortonworks](https://hortonworks.com/) distribution - checks the service status, node(s) status, stale configs, cluster alerts summary, host alerts summary, cluster health report, hdfs rack resilience configured (checks more than 1 rack configured, finds nodes with default rack configured), kerberos enabled, cluster version, service config compatible with stack and cluster

Attivio, Blue Talon, Datameer, Platfora, Zaloni plugins are also available for those proprietary products related to [Hadoop](http://hadoop.apache.org/).

#### Hadoop Distributions

- `check_cloudera_manager_*.pl` - Hadoop cluster checks via [Cloudera Manager](https://www.cloudera.com/) API - checks states and health of cluster services/roles/nodes, management services, config staleness, Cloudera Enterprise license expiry, Cloudera Manager and CDH cluster versions, utility switches to list clusters/services/roles/nodes as well as list users and their role privileges, fetch a wealth of Hadoop & OS monitoring metrics from Cloudera Manager and compare to thresholds. Disclaimer: I worked for Cloudera, but seriously CM collects an impressive amount of metrics making check_cloudera_manager_metrics.pl alone a very versatile program from which to create hundreds of checks to flexibly alert on
- [Hortonworks](https://hortonworks.com/) - the standard modern Hadoop distribution - see `check_ambari_*.pl` in the [Hadoop Ecosystem](nholuongut/nagios-nholuongut/nagios-pluginssection above
- `check_mapr*.pl` - Hadoop cluster checks via [MapR](https://mapr.com/) Control System API - checks services and nodes, MapR-FS space (cluster and per volume), volume states, volume block replication, volume snapshots and mirroring, MapR-FS per disk space utilization on nodes, failed disks, CLDB heartbeats, MapR alarms, MapReduce mode and memory utilization, disk and role balancer metrics. These are noticeably faster than running equivalent maprcli commands (exceptions: disk/role balancer use maprcli).
- `check_ibm_biginsights_*.pl` - Hadoop cluster checks via IBM BigInsights Console API - checks services, nodes, agents, BigSheets workbook runs, dfs paths and properties, HDFS space and block replication, BI console version, BI console applications deployed

#### SQL-on-Hadoop

- `check_hiveserver2*` - [Apache Hive](https://hive.apache.org/) - HiveServer2 LLAP Interactive server status and uptime, peer count, check for a specific peer host fqdn via regex and a basic beeline connection trivial query test
- `check_apache_drill_*.py/.pl` - [Apache Drill](https://drill.apache.org/) checks:
  - cluster wide: number of online / offline cluster nodes, mismatched versions across cluster
  - per drill node: status, cluster membership, encryption enabled, config settings, storage plugins enabled, version, metrics with optional thresholds
- `check_presto_*.py` - [Presto SQL DB](https://prestodb.io/)
  - cluster checks (via coordinator API) - number of current queries, running/failed/blocked/queued queries, tasks, worker nodes, failed worker nodes, workers with response lag to coordinator, workers with recent failures and recent failure ratios vs thresholds, version
  - per node checks - status, if coordinator, environment
  - per worker checks (via coordinator API) - specific worker registered with coordinator, response age to coordinator, recent requests vs threshold, recent successes, recent failures & failure ratio vs thresholds

#### Service Discovery & Coordination

- `check_zookeeper.pl` - [Apache ZooKeeper](https://zookeeper.apache.org/) server checks, multiple layers: "is ok" status, is writable (quorum), operating mode (leader/follower vs standalone), gather statistics
- `check_zookeeper_*znode*.pl` - [ZooKeeper](https://zookeeper.apache.org/) znode checks using ZK Perl API, useful for [HBase](https://hbase.apache.org/), [Kafka](https://kafka.apache.org/), [SolrCloud](https://wiki.apache.org/solr/SolrCloud), [Hadoop](http://hadoop.apache.org/) HDFS & Yarn HA (ZKFC) and any other ZooKeeper-based service. Very versatile with multiple optional checks including data vs regex, json field extraction, ephemeral status, child znodes, znode last modified age
- `check_consul_*.py` - [Consul](https://www.consul.io/) API write / read back, arbitrary key-value content checks, cluster leader election, number of cluster peers, service leader election, version
- `check_vault_*.py` - Hashicorp's [Vault](https://www.vaultproject.io/) API checks - health checks is initialized, is not standby, is vault sealed / unsealed, time skew between Vault server and local, is high availability enabled, is current leader, is leader found, version

#### Cloud

- [AWS](https://aws.amazon.com/):
  - `check_aws_s3_file.pl` - check for the existence of any arbitrary file on AWS S3, eg. to check backups have happened or _SUCCESS placeholder files are present for a job
  - `check_aws_access_keys_age.py` - checks for AWS access key age greater than N days to delete/rotate old keys as per best practice (optionally only alerts for active keys)
  - `check_aws_access_keys_disabled.py` - checks for AWS disabled access keys that should be removed
  - `check_aws_api_ping.py` - simple yes/no check for AWS API access, can be used to test access key credentials and as a dependency check for all other AWS checks
  - `check_aws_cloudtrails_enabled.py` - checks Cloud Trails have logging enabled, multi-region and logfile validation. Optionally check only a single named cloud trail
  - `check_aws_cloudtrails_event_selectors.py` - checks Cloud Trails have at least one event selector each with management and read+write logging. Optionally check only a single named cloud trail
  - `check_aws_ec2_instance_count.py` - checks the number of running instances with optional range thresholds
  - `check_aws_ec2_instance_states.py` - checks the state of all EC2 instances, outputting totals and checking warning thresholds for each status type
  - `check_aws_password_policy.py` - checks the AWS password policy including minimum length, maximum age, password reuse count, uppercase/lowercase/numbers/symbols and whether users are allowed to change their passwords
  - `check_aws_root_account.py` - checks the AWS root account has MFA enabled and no access keys as per best practice
  - `check_aws_user_last_used.py` - checks if a given AWS IAM user account has been used within the last N days (eg. if root account was recently used this may indicate a security breach or is at the very least against best practice)
  - `check_aws_users_unused.py` - detects old AWS IAM user accounts that haven't been used in the last N days, either passwords nor access keys, and should probably be removed
  - `check_aws_users_password_last_used.py` - detects AWS IAM user accounts that haven't had their passwords used in N days and should probably be removed
  - `check_aws_users_mfa_enabled.py` - checks all AWS user accounts with passwords have MFA enabled

#### Docker / Containerization

- `check_docker_*.py` - [Docker](https://www.docker.com/) API checks including API ping, counts of running / paused / stopped / total containers with thresholds, specific container status by name or id, images count with thresholds, specific image:tag availability including size and checksum, counts of networks / volumes with thresholds, docker engine version
- `check_docker_swarm_*.py` - [Docker Swarm](https://docs.docker.com/engine/swarm/) API checks including is swarm enabled, swarm node status, is the node a swarm manager, swarm service status including number of live replicas / tasks and if the service was updated recently, counts of services, swarm manager and worker nodes with thresholds, swarm errors, swarm version
- `check_mesos_*.pl` - [Mesos](http://mesos.apache.org/) master health API, master & slaves state information including leader and versions, activated & deactivated slaves, number of Chronos jobs, master & slave metrics. Warning: Mesos & Mesosphere DC/OS is legacy semi-proprietary - major momentum has shifted to the open source [Kubernetes](https://kubernetes.io/) project
- `check_kubernetes_*.py` - [Kubernetes](https://kubernetes.io/) API health and version

If running docker checks from within the [nagios plugins docker image](https://hub.docker.com/r/nholuongut/nagios-plugins/) then you will need to expose the socket within the container, like so:

```shell
$ docker run -v /var/run/docker.sock:/var/run/docker.sock nholuongut/nagios-plugins check_docker_container_status.py -H unix:///var/run/docker.sock --container myContainer
 OK: Docker container 'myContainer' status = 'running', started at '2020-06-03T14:03:09.78303932Z' | query_time=0.0038s
```

See also DockerHub build status nagios plugin further down in the [CI section](nholuongut/nagios-nholuongut/nagios-pluginstegration--build-systems---git-jenkins-travis-ci--dockerhub-automated-builds).

#### Search

- `check_elasticsearch_*.pl/.py` - [Elasticsearch](https://www.elastic.co/products/elasticsearch) cluster state, shards, replicas, number of nodes & data nodes online, shard and disk % balance between nodes, single node ok, specific node found in cluster state, slow tasks, pending tasks, elasticsearch / lucene versions, per index existence / shards / replicas / settings / age, stats per cluster / index / node, X-Pack license expiry and features enabled
  - `check_logstash_*.py` - [Logstash](https://www.elastic.co/products/logstash) status, uptime, hot threads, plugins, version, number of pipelines online, specific pipeline online and optionally its number of workers, if its dead letter queue is enabled, outputs pipeline batch size and delay
- `check_solr*.pl` - checks for [Apache Solr](http://lucene.apache.org/solr/) and [SolrCloud](https://wiki.apache.org/solr/SolrCloud) including API write/read/delete, arbitrary Solr queries vs num matching documents, API ping, Solr Core Heap / Index Size / Number of Docs for a given Solr Collection, and thresholds in ms against all Solr API operations as well as perfdata for graphing, as well as SolrCloud ZooKeeper content checks for collection shards and replicas states, number of live nodes in SolrCloud cluster, overseer, SolrCloud config and Solr metrics.

#### NoSQL

- `check_cassandra_*.pl` / `check_datastax_opscenter_*.pl` - [Apache Cassandra](http://cassandra.apache.org/) and [DataStax OpsCenter](https://www.datastax.com/) monitoring, including Cassandra cluster nodes, token balance, space, heap, keyspace replication settings, alerts, backups, best practice rule checks, DSE hadoop analytics service status and both nodetool and DataStax OpsCenter collected metrics
- `check_memcached_*.pl` - [Memcached](https://memcached.org/) API writes/reads/deletes with timings, check specific key's value against regex or value range, number of current connections, gather statistics
- `check_couchdb_*.py` - [Apache CouchDB](http://couchdb.apache.org/) API checks including server status, database exists, doc and deleted doc counts, data size, compaction running, version
- `check_riak_*.pl` - [Riak](http://basho.com/products/riak-kv/) API writes/reads/deletes with timings, check a specific key's value against regex or value range, check all riak diagnostics, check node states, check all nodes agree on ring status, gather statistics, alert on any single stat
- `check_redis_*.pl` - [Redis](https://redis.io/) API writes/reads/deletes with timings, check specific key's value against regex or value range, replication slaves I/O, replicated writes (write on master -> read from slave), publish/subscribe, connected clients, validate redis.conf against running server to check deployments or remote compliance checks, gather statistics, alert on any single stat

#### SQL Databases

- `check_mysql_query.pl` - flexible free-form [MySQL](https://www.mysql.com/) SQL queries - can check almost anything - obsoleted a dozen custom MySQL plugins and prevented writing many more. Tested against many versions of [MySQL](https://www.mysql.com/) and [MariaDB](https://mariadb.org/). You may also be interested in [Percona's plugins](https://www.percona.com/doc/percona-monitoring-plugins/latest/index.html)
- `check_mysql_config.pl` - detect differences in your /etc/my.cnf and running MySQL config to catch DBAs making changes to running databases without saving to /etc/my.cnf or backporting to Puppet. Can also be used to remotely validate configuration compliance against a known good baseline. Tested against many versions of [MySQL](https://www.mysql.com/) and [MariaDB](https://mariadb.org/)

##### Publish - Subscribe / Message Queues

These programs check these message brokers end-to-end via their API, by acting as both a producer and a consumer and checking that a unique generated message passes through the broker cluster and is received by the consumer at the other side successfully. They report the publish, consumer and total timings taken, against which thresholds can be applied, and are also available as perfdata for graphing.

- `check_kafka.py/.pl` - [Kafka](https://kafka.apache.org/) brokers API write & read back with configurable topics/partition and producer behaviour for acks, sleep, retries, backoff, can also lists topics and partitions. See [Kafka Scala Nagios Plugin](https://github.com/nholuongut/Nagios-Plugin-Kafka) for a version with Kerberos support
- `check_redis_publish_subscribe.pl` - [Redis](https://redis.io/) publish-subscribe API write & read back with configurable subscriber wait. See other Redis checks under [NoSQL](nholuongut/nagios-nholuongut/nagios-plugins
- `check_rabbitmq*.py` - [RabbitMQ](https://www.rabbitmq.com/) brokers AMQP API write & read back with configurable vhost, exchange, exchange type, queue, routing key, durability, RabbitMQ 'confirms' protocol extension & standard AMQP transactions support. Checks via the RabbitMQ management API include aliveness queue health test, built-in health checks, cluster name, vhost, exchange with optional validation of exchange type (direct, fanout, headers, topic) and durability (true/false), user auth and permissions tags, stats db event queue

<!--
Debian / Ubuntu systems also have other unrelated RabbitMQ plugins in the `nagios-plugins-rabbitmq` package
-->

#### CI - Continuous Integration & Build Systems - Git, Jenkins, Travis CI & DockerHub Automated Builds

- `check_jenkins_*.py` - [Jenkins](https://jenkins.io/) checks include job build status, color, health report score, build time, age since last completed build, if job is set to buildable, job count total or per view, number of running builds, queued builds, executors, node count, offline nodes, jenkins mode, is security enabled, if a given node is online and its number of executors, if a given plugin is enabled and if there are available plugin updates individually or overall, with perfdata for relevant metrics like build time, jobs/nodes/executors/plugins/plugin updates, running/queued build counts and query timings
- `check_travis_ci_last_build.py` - [Travis CI](https://travis-ci.org/) repo's last build status - includes showing build number, build duration with optional thresholds, start/stop date & time, if there are currently any builds in progress and perfdata for graphing last build time and number of builds in progress. Verbose mode gives the commit details as well such as commit id and message
- `check_gocd_*.py` - [GoCD](https://www.gocd.org/) server and agent health, pipeline, stage and job level status checks, and number of agents online, enabled, and in different states
- `check_dockerhub_repo_build_status.py` - [DockerHub](https://hub.docker.com/u/nholuongut/) Automated Build status check for a given DockerHub repository's latest build or latest build for a given tag. Returns status and tag of last build along with perfdata for graphing build latency (time between build creation and completion) and query timing. Optionally also returns in verbose mode what triggered the build (webhook, revision control change, API / website trigger), created and last updated date timestamps and build URL to investigate
- `check_selenium_*.py` - checks [Selenium Grid](https://www.selenium.dev/documentation/en/grid/) Hub / Node or [Selenoid](https://aerokube.com/selenoid/) status is ready, queue size, available node counts for all or specific browser types, and that browsers are available and fully functional by requesting a browser (eg. chrome or firefox), querying a url and optionally performing a content or regex match on the returned web page
- `check_git_*` - checks a [Git](https://git-scm.com/) checkout is valid, up to date with upstream remote/origin, has no uncommitted changes (staged or unstaged), no untracked files, isn't dirty, is in the right branch, isn't remote, isn't detached, is / isn't bare. Useful for monitoring deployment servers running off Git checkouts (a common scenario for things like [PuppetMasters](https://puppet.com/), [Ansible](https://www.ansible.com/) [AWX](https://github.com/ansible/awx) / [Tower](https://www.ansible.com/products/tower) etc) to ensure your automation is deploying the right thing and that any ad-hoc modifications and tests have been properly backported to Git

#### Infrastructure - Internet - Web, DNS, SSL, Domains

- `check_ssl_cert.pl` - SSL certificate checker - checks certificate expiry (days), validates domain, chain of trust, SNI, wildcard domains, SAN certs with multi-domain support. Chain of Trust support is important when building your JKS or certificate bundles to include intermediate certs otherwise certain mobile devices don't validate the SSL even though it may work in your desktop browser
- `check_dns.pl` - advanced DNS query checker supporting NS records for your public domain name, MX records for your mail servers, SOA, SRV, TXT as well as A and PTR records. Can optionally specify `--expected` literal or `--regex` results (which is anchored for security) for strict validation to ensure all records returned are expected and authorized. The record, type and result(s) are output along with the DNS query timing perfdata for graphing DNS performance
- `check_whois.pl` - check domain expiry days left and registration details match expected
- `check_pingdom_*.py` - checks [Pingdom](https://www.pingdom.com/) statuses, response times, last checked times, SMS credits

#### Infrastructure - Linux - OS, Network, Puppet, RAID, SSH, Clusters, Yum Security Updates

- `check_puppet.rb` - thorough, find out when [Puppet](https://puppet.com/) stops properly applying manifests, if it's in the right environment, if it's --disabled, right puppet version etc
- `check_disk_write.pl` - canary write test, catches partitions getting auto-remounted read-only by Linux when it detects underlying storage I/O errors (often caused by malfunctioning block devices, raid arrays, failing disks), see also `check_linux_disk_mounts_read_only.py`
- `check_linux_*.pl/.py` - checks RAM used, CPU context switches, system file descriptors, interface errors / promiscous mode / duplex / speed / MTU / stats, load normalized per CPU core (more useful than the default check_load plugin which would need different configs for heterogenous hardware), timezone settings, users / groups present (eg. PAM/LDAP/SSSD integration is working), duplicate UID/GIDs (helps detects rogue uid 0 accounts and more common LDAP vs local id range overlap misconfigurations), check groups.allow contains only specific groups, huge pages are disabled (often recommended for Big Data and NoSQL systems such as Hadoop and MongoDB), any read-only filesystems (more of a sweep than `check_disk_write.pl`, with include/exclude regex)
- `check_ssh_login.pl` - performs a full SSH login with username & password, good for testing your Dell DRAC / HP iLO infrastructure is properly secured and accessible. Also works for your Linux servers and even Mac OSX
- `older/check_*raid.py` - RAID controller / array checks for 3ware, LSI MegaRaid / Dell PERC controllers (they're rebranded from LSI), and Linux software MD Raid. I also recommend the widely used [Dell OpenManage Check](http://folk.uio.no/trondham/software/check_openmanage.html)
- `check_*_version*.pl/.py` - checks running versions of software - originally written to detect version inconsistencies across large clusters of servers and failed/partial upgrades across large automated infrastructures. Now also used to check [Docker](https://www.docker.com/) tagged images contain the right versions of the expected software (which double validates that other programs in this and other github repos have actually been tested against all the expected versions)
- `check_cluster_version.pl` can be used to tie together versions returned from many different servers (by passing it their outputs via Nagios macros) to ensure a cluster is all running the same version of software even if you don't enforce a particular `--expected` version on individual systems
- `check_yum.py/.pl` - widely used yum security updates checker for RHEL 5 - 8 systems dating back to 2008. You'll find forks of this around including NagiosExchange but please re-unify on this central updated version. Also has a Perl version which is a newer straight port with nicer more concise code and better library backing as well as configurable self-timeout. For those running Debian-based systems like Ubuntu see `check_apt` from the `nagios-plugins-basic` package.

... and there are many more plugins than we have space to list here, have a browse!

This code base is under active development and there are many more cool plugins pending import.

See also [other 3rd Party Nagios Plugins](nholuongut/nagios-nholuongut/nagios-pluginsios-plugins) you might be interested in.

#### Compatibility / Translation Plugins

These allow you to use any standard nagios plugin with other non-Nagios style monitoring systems by prefixing the nagios plugin command with these programs, which will execute and translate the outputs:

- `adapter_csv.py` - executes and translates output from any standard nagios plugin to CSV format
- `adapter_check_mk.py` - executes and translates output from any standard nagios plugin to Check_MK local plugin format
- `adapter_geneos.py` - executes and translates output from any standard nagios plugin to Geneos CSV format

### Usage --help

All plugins come with `--help` which lists all options as well as giving a program description, often including a detailed account of what is checked in the code. You can also find example commands in the `tests/` directory.

Environment variables are supported for convenience and also to hide credentials from being exposed in the process list eg. `$PASSWORD`. These are indicated in the `--help` descriptions in brackets next to each option and often have more specific overrides with higher precedence eg. `$ELASTICSEARCH_HOST` takes priority over `$HOST`, `$REDIS_PASSWORD` takes priority over `$PASSWORD` etc.

Make sure to run the [automated build](nholuongut/nagios-nholuongut/nagios-pluginsom-source) or install the required Perl CPAN / Python PyPI modules first before calling `--help`.

### Kerberos Security Support

Perl HTTP Rest-based plugins have implicit Kerberos support via LWP as long as the LWP::Authen::Negotiate CPAN module is installed (part of the automated `make` build). This will look for a valid TGT in the environment (`$KRB5CCNAME`) and if found will use it for SPNego.

Most Python HTTP Rest-based plugins for technologies / APIs with authentication have a `--kerberos` switch which supercedes `--username/--password` and can be used on technologies that support SPNego Kerberos authentication. It will either use the TGT from the environment cache (`$KRB5CCNAME`) or if `$KRB5_CLIENT_KTNAME` is present will kinit from the keytab specified in `$KRB5_CLIENT_KTNAME` to a unique path per plugin to prevent credential cache clashes if needing to use different credentials for different technologies.

Automating Kerberos Tickets - if running a plugin by hand for testing then you can initiate your TGT via the `kinit` command before running the plugin but if running automatically in a monitoring server then use the standard `k5start` kerberos utility as a service to auto-initiate and auto-renew your TGT so that your plugins always authenticate to Kerberized services with a current valid TGT.

To use different kerberos credentials per plugin you can `export KRB5CCNAME=/different/path` before executing each plugin, and have multiple `k5start` instances maintaining each one.

### High Availability / Multi-Master testing

Testing high availability and multi-master setups is best done through a load balancer.

HAProxy configurations are provided for all the major technologies under the [haproxy-configs/](https://github.com/nholuongut/HAProxy-configs) directory for many of the technologies tested in this project, including:

- Hadoop HDFS NameNodes
- Hadoop Yarn Resource Managers
- HBase Masters, Stargate Rest & Thrift servers
- Cassandra
- Apache Drill
- Impala
- Presto SQL Coordinators
- Kubernetes API
- Oozie
- SolrCloud
- Elasticsearch

#### See Also

The following is pulled from my [DevOps Python Tools repo](https://github.com/nholuongut/devps-python-tools) (currently one of my favourite repos):

- `find_active_server.py` - returns the first available healthy server or determines the active master in high availability setups. Configurable tests include socket, http, https, ping, url with optional regex content match and is multi-threaded for speed. Useful for pre-determining a server to be passed to tools that only take a single `--host` argument but for which the technology has later added multi-master support or active-standby masters (eg. Hadoop, HBase) or where you want to query cluster wide information available from any online peer (eg. Elasticsearch, RabbitMQ clusters). This is downloaded from my [DevOps Python Tools repo](https://github.com/nholuongut/devps-python-tools) as part of the build and placed at the top level. It has the ability to extend any nagios plugin to support multiple hosts in a generic way if you don't have a front end load balancer to run the check through. Example usage:

```shell
./check_elasticsearch_cluster_status.pl --host $(./find_active_server.py --http --port 9200 node1 node2 node3)
```

There are now also simplified subclassed programs so you don't have to figure out the switches for more complex services like Hadoop and HBase, just provide hosts as simple arguments and they'll return the current active master!

- `find_active_hadoop_namenode.py`
- `find_active_hadoop_yarn_resource_manager.py`
- `find_active_hbase_master.py`
- `find_active_hbase_thrift.py`
- `find_active_hbase_stargate.py`
- `find_active_cassandra.py`
- `find_active_apache_drill.py`
- `find_active_impala.py`
- `find_active_presto_coordinator.py`
- `find_active_kubernetes_api.py`
- `find_active_oozie.py`
- `find_active_solrcloud.py`
- `find_active_elasticsearch.py`

These are especially useful for ad-hoc scripting or quick command line tests.

### Configuration for Strict Domain / FQDN validation

Strict validations include host/domain/FQDNs using TLDs which are populated from the official IANA list. This is done via the [Lib](https://github.com/nholuongut/lib) and [PyLib](https://github.com/nholuongut/pylib) submodules for Perl and Python plugins respectively - see those repos for details on configuring to permit custom TLDs like `.local` or `.intranet` (both already supported by default as they're quite common customizations).

### Quality

Most of the plugins I've read from [Nagios Exchange](https://exchange.nagios.org/) and Monitoring Exchange (now [Icinga Exchange](https://exchange.icinga.org/)) in the last decade have not been of the quality required to run in production environments I've worked in (ever seen plugins written in Bash with little validation, or mere 200-300 line plugins without robust input/output validation and error handling, resulting in "UNKNOWN: (null)" when something goes wrong - right when you need them - then you know what I mean). That prompted me to write my own plugins whenever I had an idea or requirement.

That naturally evolved in to this, a relatively Advanced Collection of Nagios Plugins, especially when I began standardizing and reusing code between plugins and improving the quality of all those plugins while doing so.

#### Goals

- specific error messages to aid faster Root Cause Analysis
- consistent behaviour
- standardized switches
- strict input/output validation at all stages, written for security and robustness
- code reuse, especially for more complex input/output validations and error handling
- multiple `--verbose` levels & `--debug` mode
- `--warning/--critical` thresholds with range support, in form of `min:max` (`@` prefix inverts to expect value outside of this range)
- support for use of `$USERNAME` and `$PASSWORD` environment variables as well as more specific overrides (eg. `$MYSQL_USERNAME`, `$REDIS_PASSWORD`) to give administrators the option to avoid leaking `--password` credentials in the process list for all users to see
- self-timeouts
- [Metrics Graphing integrations](nholuongut/nagios-nholuongut/nagios-pluginsntegrations)  - [Graphite](https://graphiteapp.org/), [InfluxDB](https://www.influxdata.com/), [OpenTSDB](http://opentsdb.net/) and [PNP4Nagios](https://docs.pnp4nagios.org/) can all auto-graph the perfdata from these plugins
- [Continuous Integration](https://travis-ci.org/nholuongut/nagios-plugins) with tests for success and failure scenarios:
  - unit tests for the custom supporting [perl](https://github.com/nholuongut/lib) and [python](https://github.com/nholuongut/pylib) libraries
  - integration tests of the top level programs using the libraries for things like option parsing
  - [functional tests](nholuongut/nagios-nholuongut/nagios-plugins for the top level programs using [Docker containers](https://hub.docker.com/u/nholuongut/) for each technology (eg. Cassandra, Elasticsearch, Hadoop, HBase, ZooKeeper, Memcached, Neo4j, MongoDB, MySQL, Riak, Redis...)
- easy rapid development of new high quality robust Nagios plugins with minimal lines of code

Several plugins have been merged together and replaced with symlinks to the unified plugins bookmarking their areas of functionality, similar to some plugins from the standard nagios plugins collection.

Some plugins such as those relating to Redis and Couchbase also have different modes and expose different options when called as different program names, so those symlinks are not just cosmetic. An example of this is write replication, which exposes extra options to read from a slave after writing to the master to check that replication is 100% working.

Perl ePN optimization is not supported at this time as I was running 13,000 production checks per Nagios server years ago (circa 2010) without ePN optimization - it's not worth the effort and isn't available in any of the other languages anyway.

Python plugins are all pre-byte-compiled as part of the automated build.

Modern scaling should be done using distributed computing, open source examples include [Icinga2](https://www.icinga.com/docs/icinga2/latest/doc/06-distributed-monitoring/) and [Shinken](http://shinken.readthedocs.io/en/latest/07_advanced/scaling-shinken.html#advanced-scaling-shinken). Shinken's [documentation](http://shinken.readthedocs.io/en/latest/07_advanced/distributed-shinken.html?highlight=150000%20checks/5min) cites an average 4 core server @ 3Ghz as supporting 150,000 checks per 5 minutes, which aligns with my own experience with Nagios Core. Using the latest hardware and proper setup could probably result in even higher scale before having to move to distributed monitoring architecture.

##### Libraries

Having written a large number of Nagios Plugins in the last 10 years in a variety of languages (Python, Perl, Ruby, Bash, VBS) I abstracted out common components of a good robust Nagios Plugin program in to libraries of reusable components that I leverage very heavily in all my modern plugins and other programs found under my other repos here on GitHub, which are now mostly written in Perl or Python using these custom libraries, for reasons of both concise rapid development and speed of execution.

These libraries enables writing much more thoroughly validated production quality code, to achieve in a quick 200 lines of Perl or Python what might otherwise take 2000-3000 lines to do properly (including some of the more complicated supporting code such as robust validation functions with long complex regexs with unit tests, configurable self-timeouts, warning/critical threshold range logic, common options and generated usage, multiple levels of verbosity, debug mode etc), dramatically reducing the time to write high quality plugins down to mere hours and at the same time vastly improving the quality of the final code through code reuse, as well as benefitting from generic future improvements to the underlying libraries.

This gives each plugin the misleading appearance of being very short, because only the some of the very core logic of what you're trying to achieve is displayed in the plugin itself, mostly composition of utility functions, and the error handling is often handled in custom libraries too, so it may appear that a simple one line field extraction or 'curl()' or 'open_file()' utility function call has no error handling at all around it but under the hood the error handling is handled inside the function inside a library, same for HBase Thrift API connection, Redis API connection etc so the client code as seen in the top level plugins knows it succeeded or otherwise the framework would have errored out with a specific error message such as "connection refused" etc... there is a lot of buried error checking code and a lot of utility functions so many operations become one-liners at the top level instead of huge programs that are hard to read and maintain.

I've tried to keep the quality here high so a lot of plugins I've written over the years haven't made it in to this collection, there are a lot still pending import, a couple others `check_nsca.pl` and `check_syslog-ng_stats.pl` are in the `more/` directory until I get round to reintegrating and testing them with my current framework to modernize them, although they should still work with the tiny utils.pm from the standard nagios plugins collection.

I'm aware of Nagios::Plugin but my libraries have a lot more utility functions and I've written them to be highly convenient to develop with.

##### Older Plugins

Some older plugins may not adhere to all of the criteria above so most have been filed away under the `older/` directory (they were used by people out there in production so I didn't want to remove them entirely). Older plugins also indicate that I haven't run or made updates to them in a few years so they're in basic maintenance mode and may require minor tweaks or updates.

If you're new remember to check out the `older/` directory for more plugins that are less current but that you might find useful such as RAID checks for Linux MD Raid, 3ware / LSI MegaRaid / Dell Perc Raid Controllers (which are actually rebranded LSI MegaRaid so you can use the same check - I also recommend the widely used [Dell OpenManage Check](http://folk.uio.no/trondham/software/check_openmanage.html)).

### Contributions

Feedback, Feature Requests, Improvements and Patches are welcome.

Patches are accepted in the form of [Github pull requests](nholuongut/nagios-nholuongut/nagios-pluginsyou will receive attribution automatically as Github tracks these merges.

### Support for Updates / Bugs Fixes / Feature Requests

Please raise a [Github Issue ticket](nholuongut/nagios-nholuongut/nagios-plugins need updates, bug fixes or new features. [Github pull requests](nholuongut/nagios-plugins/pulls) are mnholuongut/nagios-plugins

Since there are a lot of programs covering a lot of different technologies in this project, so remember to look at the software versions each program was written / tested against (documented in --help for each program, also found near the top of the source code in each program). Newer versions of software seem to change a lot these days especially in the Big Data & NoSQL space so plugins may require updates for newer versions.

Please make sure you have run `make update` first to pull the latest updates including library sub-modules and build the latest CPAN / PyPI module dependencies, (see [Quick Setup](nholuongut/nagios-nholuongut/nagios-plugins).

Make sure you run the code by hand on the command line with `-v -v -v` for additional debug output and paste the full output in to the issue ticket. If you want to anonymize your hostnames/IP addresses etc you may use the `scrub.pl` tool found in my [DevOps Perl Tools repo](https://github.com/nholuongut/DevOps-Perl-tools).

### Detailed Build Instructions

#### Automated Build

```shell

git clone nholuongut/nagios-nholuongut/nagios-plugins

cd nagios-plugins

make build

```

Some plugins like `check_yum.py` can be copied around independently but most newer more sophisticated plugins require the co-located libraries I've written so you should `git clone && make` on each machine you deploy this code to or just use the pre-built [Docker image](https://hub.docker.com/r/nholuongut/nagios-plugins) which has all plugins and dependencies inside.

You may need to install the GNU make system package if the `make` command isn't found (`yum install make` / `apt-get install make`)

To build just the Perl or Python dependencies for the project you can do ` make perl ` or ` make python `.

If you only want to use one plugin, you can do ` make perl-libs ` or ` make python-libs ` and then just install the potential one or two dependencies specific to that one plugin if it has any, which is much quicker than building the whole project.

` make ` builds will install yum rpms / apt debs dependencies automatically as well as a load of Perl CPAN & Python PyPI libraries. To pick and choose what to install follow the [Manual Build](nholuongut/nagios-nholuongut/nagios-pluginsion instead

This has become quite a large project and will take at least 10 minutes to build. The build is automated and tested on RHEL / CentOS 5/6/7 & Debian / Ubuntu systems.

Make sure /usr/local/bin is in your ` $PATH ` when running make as otherwise it'll fail to find ` cpanm `

##### Python VirtualEnv / Perlbrew localized installs

The automated build will use 'sudo' to install required Perl CPAN & Python PyPI libraries to the system unless running as root or it detects being inside Perlbrew or VirtualEnv. If you want to install some of the common Perl / Python libraries such as Net::DNS and LWP::* using your OS packages instead of installing from CPAN / PyPI then follow the [Manual Build](nholuongut/nagios-nholuongut/nagios-pluginsion instead.

#### Offline Setup

Download the Nagios Plugins, Lib and Pylib git repos as zip files:

<nholuongut/nagios-nholuongut/nagios-plugins>

<https://github.com/nholuongut/lib/archive/master.zip>

<https://github.com/nholuongut/pylib/archive/master.zip>

Unzip all and move Lib and Pylib to the `lib` and `pylib` folders under nagios plugins.

```shell
unzip nagios-plugins-master.zip
unzip pylib-master.zip
unzip lib-master.zip

mv -v nagios-plugins-master nagios-plugins
mv -v pylib-master pylib
mv -v lib-master lib
mv -vf pylib nagios-plugins/
mv -vf lib nagios-plugins/
```

Proceed to install CPAN and PyPI modules for whichever programs you want to use using your usual procedure - usually an internal mirror or proxy server to CPAN and PyPI, or rpms / debs (some libraries are packaged by Linux distributions).

All CPAN modules are listed in `setup/cpan-requirements*.txt` and `lib/setup/cpan-requirements*.txt`.

All PyPI modules are listed in `requirements.txt` and `pylib/requirements.txt`.

Internal PyPI Mirror example ([JFrog Artifactory](https://jfrog.com/artifactory/), [CloudRepo](https://cloudrepo.io) or similar):

```shell
sudo pip install --index https://host.domain.com/api/pypi/repo/simple --trusted host.domain.com -r requirements.txt -r pylib/requirements.txt
```

Proxy example:

```shell
sudo pip install --proxy hari:mypassword@proxy-host:8080 -r requirements.txt -r pylib/requirements.txt
```

##### Mac OS X

The automated build also works on Mac OS X but you will need to download and install [Apple XCode](https://developer.apple.com/download/) development libraries. I also recommend you get [HomeBrew](https://brew.sh/) to install other useful tools and libraries you may need like OpenSSL, Snappy and MySQL for their development headers and tools such as wget (these packages are automatically installed if Homebrew is installed on Mac OS X):

```shell
brew install openssl snappy mysql wget
```

###### OpenSSL Fixes

###### Perl CPAN Crypt::SSLeay

To avoid the following cpan install error:

```none
fatal error: 'openssl/opensslv.h' file not found
#include <openssl/opensslv.h>
```

specify the path to the OpenSSL lib installed by HomeBrew:

```none
sudo OPENSSL_INCLUDE=/usr/local/opt/openssl/include OPENSSL_LIB=/usr/local/opt/openssl/lib cpan Crypt::SSLeay
```

###### Perl CPAN DBD::mysql

Ensure the `DBI` cpan module is installed as well as the `openssl` HomeBrew package.

You may need to add the OpenSSL library path explicitly in `mysql_config` to avoid the following error:

```shell
Checking if libs are available for compiling...
Can't link/include C library 'ssl', 'crypto', aborting.
```

Once you're sure that OpenSSL is installed via HomeBrew (done as part of the automated build), find `mysql_config` and edit the line

```none
libs="-L$pkglibdir"
```

to

```none
libs="-L$pkglibdir -L/usr/local/opt/openssl/lib"
```

##### Python Pip

You may get errors trying to install to Python library paths even as root on newer versions of Mac, sometimes this is caused by pip 10 vs pip 9 and downgrading will work around it:

```shell
sudo pip install --upgrade pip==9.0.1
make
sudo pip install --upgrade pip
make
```

#### ZooKeeper Checks

If you want to use any of the ZooKeeper content znode based checks (eg. for HBase / SolrCloud etc) based on check_zookeeper_znode.pl or any of the check_solrcloud_*_zookeeper.pl programs you will also need to install the zookeeper libraries which has a separate build target due to having to install C bindings as well as the library itself on the local system. This will explicitly fetch the tested ZooKeeper 3.4.8, you'd have to update the `ZOOKEEPER_VERSION` variable in the Makefile if you want a different version.

```shell
make zookeeper
```

This downloads, builds and installs the ZooKeeper C bindings which Net::ZooKeeper needs. To clean up the working directory afterwards run:

```shell
make clean-zookeeper
```

### Manual Build

Fetch my library repos which are included as submodules (they're shared between this and other repos containing various programs I've written over the years).

```shell

git clone nholuongut/nagios-nholuongut/nagios-plugins

cd nagios-plugins

git submodule init

git submodule update

```

Then install the Perl CPAN and Python PyPI modules as listed in the next sections.

For Mac OS X see the [Mac OS X](nholuongut/nagios-nholuongut/nagios-pluginsfrom Automated Build instructions.

#### Perl CPAN Modules

If installing the Perl CPAN or Python PyPI modules via your package manager or by hand instead of via the [Automated Build From Source](nholuongut/nagios-nholuongut/nagios-pluginsom-source) section, then read the [requirements.txt](nholuongut/nagios-plugins/blob/master/nholuongut/nagios-pluginstup/cpan-requirements.txt](nholuongut/nagios-plugins/blob/master/setup/cpan-requiremnholuongut/nagios-pluginsists of Python PyPI and Perl CPAN modules respectively that you need to install.

You can install the full list of CPAN modules using this command:

```shell
sudo cpan $(sed 's/#.*//' setup/cpan-requirements*.txt lib/setup/cpan-requirements*.txt)
```

and install the full list of PyPI modules using this command:

```shell
sudo pip install -r requirements.txt -r pylib/requirements.txt
```

##### Net::ZooKeeper (for various ZooKeeper content checks for Kafka, HBase, SolrCloud etc)

```shell
check_zookeeper_znode.pl
check_zookeeper_child_znodes.pl
check_hbase_*_znode.pl
check_solrcloud_*_zookeeper.pl
```

The above listed programs require the Net::ZooKeeper Perl CPAN module but this is not a simple `cpan Net::ZooKeeper`, that will fail. Follow these instructions precisely or debug at your own peril:

```shell
# install C client library
export ZOOKEEPER_VERSION=3.4.8
[ -f zookeeper-$ZOOKEEPER_VERSION.tar.gz ] || wget -O zookeeper-$ZOOKEEPER_VERSION.tar.gz http://www.mirrorservice.org/sites/ftp.apache.org/zookeeper/zookeeper-$ZOOKEEPER_VERSION/zookeeper-$ZOOKEEPER_VERSION.tar.gz
tar zxvf zookeeper-$ZOOKEEPER_VERSION.tar.gz
cd zookeeper-$ZOOKEEPER_VERSION/src/c
./configure
make
sudo make install

# now install Perl module using C library with the correct linking
cd ../contrib/zkperl
perl Makefile.PL --zookeeper-include=/usr/local/include/zookeeper --zookeeper-lib=/usr/local/lib
LD_RUN_PATH=/usr/local/lib make
sudo make install
```

After this check it's properly installed by doing

```shell
perl -e "use Net::ZooKeeper"
```

which should return no errors if successful.

### Other Dependencies

Some plugins, especially ones under the older/ directory such as those that check 3ware/LSI raid controllers, SVN, VNC etc require external binaries to work, but the plugins will tell you if they are missing. Please see the respective vendor websites for 3ware, LSI etc to fetch those binaries and then re-run those plugins.

The `check_puppet.rb` plugin uses Puppet's native Ruby libraries to parse the Puppet config and as such will only be run where Puppet is properly installed.

The `check_logserver.py` "Syslog to MySQL" plugin will need the Python MySQL module to be installed which you should be able to find via your package manager. If using RHEL/CentOS do:

```shell
sudo yum install MySQL-python
```

or try install via pip, but this requires MySQL to be installed locally in order to build the Python egg...

```shell
sudo easy_install pip
sudo pip install MySQL-python
```

### Updating

Run `make update`. This will git pull and then git submodule update which is necessary to pick up corresponding library updates.

If you update often and want to just quickly git pull + submodule update but skip rebuilding all those dependencies each time then run `make update-no-recompile` (will miss new library dependencies - do full `make update` if you encounter issues).

#### Testing

There are full multi-level suites of tests against this repository and its libraries.

[Continuous Integration](https://travis-ci.org/nholuongut/nagios-plugins) is run on this repo with tests for success and failure scenarios:

- Unit Tests - 1200+ unit tests covering the [Perl library](https://github.com/nholuongut/lib) and [Python library](https://githu.com/nholuongut/pylib)
- Integration tests checking dependency integration, usage `--help` generation etc.
- Custom tests for various languages and build systems, linting, coding style, and other standardizations
- Functional Tests - 800+ full functional [tests/](nholuongut/nagios-nholuongut/nagios-plugins using dozens of [Docker Images](https://hub.docker.com/u/nholuongut/) for full API testing of the various technologies

To trigger all tests run:

```shell
make test
```

which will start with the underlying libraries, then move on to top level integration tests and finally functional tests using docker containers if docker is available.

#### Bugs & Workarounds

##### Kafka dependency NetAddr/IP/InetBase autoload bug

If you encounter the following error when trying to use `check_kafka.pl`:

```none
Can't locate auto/NetAddr/IP/InetBase/AF_INET6.al in @INC
```

This is an upstream bug related to autoloader, which you can work around by editing `NetAddr/IP/InetBase.pm` and adding the following line explicitly near the top just after `package NetAddr::IP::InetBase;`:

```perl
use Socket;
```

On Linux this is often at `/usr/local/lib64/perl5/NetAddr/IP/InetBase.pm` and on Mac `/System/Library/Perl/Extras/<version>/NetAddr/IP/InetBase.pm`.
You can find the location using `perl_find_library_path.pl NetAddr::IP::InetBase` or `perl_find_library_path.sh NetAddr::IP::InetBase` from the [DevOps Perl Tools](https://github.com/nholuongut/DevOps-Perl-tools) and [DevOps Bash Tools](https://github.com/nholuongut/DevOps-Bash-tools) repos.

You may also need to install Socket6 from CPAN.

This fix is now fully automated in the Make build by patching the `NetAddr/IP/InetBase.pm` file and always including Socket6 in dependencies (UPDATE: this fix is broken on recent versions of Mac due to the addition of System Integrity Protection which doesn't allow editing the system files even with sudo to root - a workaround would be to install the libraries to a local PERLBREW and fix there).

Alternatively you can try the Python version `check_kakfa.py` which works in similar fashion.

##### MongoDB dependency Readonly library bug

The MongoDB Perl driver from CPAN doesn't seem to compile properly on RHEL5 based systems. PyMongo rewrite was considered but the extensive library of functions results in better code quality for the Perl plugins, it's easier to just upgrade your OS to RHEL6.

The MongoDB Perl driver does compile on RHEL6 but there is a small bug in the Readonly CPAN module that the MongoDB CPAN module uses. When it tries to call Readonly::XS, a MAGIC_COOKIE mismatch results in the following error:

```none
Readonly::XS is not a standalone module. You should not use it directly. at /usr/local/lib64/perl5/Readonly/XS.pm line 34.
```

The workaround is to edit the Readonly module and comment out the `eval 'use Readonly::XS'` on line 33 of the Readonly module.

This is located here on Linux:

```none
/usr/local/share/perl5/Readonly.pm
```

and here on Max OS X:

```none
/Library/Perl/5.16/Readonly.pm
```

##### IO::Socket::SSL doesn't respect ignoring self-signed certs in recent version(s) eg. 2.020

Recent version(s) of IO::Socket::SSL (2.020) seem to fail to respect options to ignore self-signed certs. The workaround is to create the hidden touch file below in the same top-level directory as the library to make this it include and use Net::SSL instead of IO::Socket::SSL.

```shell
touch .use_net_ssl
```

#### Python SSL certificate verification problems

If you end up with an error like:

```none
[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:765)
```

It can be caused by an issue with the underlying Python + libraries due to changes in OpenSSL and certificates. One quick fix is to do the following:

```shell
sudo pip uninstall -y certifi &&
sudo pip install certifi==2015.04.28
```

### Enterprise Monitoring Systems

#### Compatible Monitoring Solutions

The biggest advantage of Nagios-compatible monitoring systems is the multitude of Nagios Plugins created by domain experts in each field to monitor almost everything out there.

Nagios Plugins are widely and freely available across the internet, especially at the original [Nagios Exchange](https://exchange.nagios.org/) and the newer [Icinga Exchange](https://exchange.icinga.com/) (at which you'll see this project at the top of the most viewed list).

The following enterprise monitoring systems are compatible with Nagios Plugins and this project:

- [Nagios Core](https://www.nagios.org/) - the original widely used open source monitoring system that set the standard
  - [Nagios Command Configuration](http://nagios.sourceforge.net/docs/3_0/objectdefinitions.html#command)
  - [Nagios Service Configuration](http://nagios.sourceforge.net/docs/3_0/objectdefinitions.html#service)
  - [NRPE - Nagios Remote Plugin Executor](https://assets.nagios.com/downloads/nagioscore/docs/nrpe/NRPE.pdf) - most plugins check network services like NoSQL datastores but you can use NRPE for plugins that check the local system eg. `check_linux_*` / `older/check_*raid*.py`)
  - [PNP4Nagios](http://docs.pnp4nagios.org/start) - widely used metrics auto graphing add-on for Nagios

- [Nagios IX](https://www.nagios.com/products/nagios-xi/) - commercial version of the open source Nagios Core with more features and enterprise support. Most people using Nagios use the free version since most of the benefit is in the plugins themselves.

- [Icinga2](https://www.icinga.org/) - popular open source Nagios fork rewritten with more features, Icinga retains the all important Nagios Plugin compatibility, but also has native [distributed monitoring](https://www.icinga.com/docs/icinga2/latest/doc/06-distributed-monitoring/), [rule based configuration](https://www.icinga.com/2014/03/31/icinga-2-0-0-9-introducing-configuration-apply-rules/), a REST API and native metrics graphing integrations via [Graphite](https://www.icinga.com/docs/icinga2/latest/doc/09-object-types/#graphitewriter), [InfluxDB](https://www.icinga.com/docs/icinga2/latest/doc/09-object-types/#influxdbwriter) and [OpenTSDB](https://www.icinga.com/docs/icinga2/latest/doc/09-object-types/#opentsdbwriter) to create graphs from the plugins' perfdata

- [Shinken](http://www.shinken-monitoring.org/) - open source modular Nagios reimplementation in Python, Nagios config compatible, with distributed monitoring architecture, high availability, host / service discovery, forwards plugins' metrics perfdata via the Graphite protocol to [Graphite](https://graphiteapp.org/) or [InfluxDB](https://www.influxdata.com/), see [documentation](http://shinken.readthedocs.io/en/latest/11_integration/graphite.html)

- [Centreon](https://www.centreon.com/en/) - open source french Nagios-compatible monitoring solution, can forward plugin's metrics perfdata to [Graphite](https://graphiteapp.org/) or [InfluxDB](https://www.influxdata.com/) via Graphite protocol, see [documentation](https://documentation.centreon.com/docs/centreon-broker/en/3.0/user/modules.html#graphite)

- [Naemon](http://www.naemon.org/) - open source Nagios-forked monitoring solution, using [Thruk](http://thruk.org/) as its GUI and [PNP4Nagios](http://docs.pnp4nagios.org/start) for graphing the plugins' metrics perfdata

- [OpenNMS](https://opennms.org/en) - open source enterprise-grade network management platform with native graphing, geo-mapping, Grafana integration, as well as Elasticsearch event forwarder integration for Kibana search/visualization. OpenNMS can execute Nagios Plugins via NRPE, see [NRPEMonitor documentation](http://docs.opennms.org/opennms/releases/latest/guide-admin/guide-admin.html#_nrpemonitor)

- [Pandora FMS](https://pandorafms.com/) - open source distributed monitoring solution with flexible dashboarding, graphing, SLA reporting and Nagios Plugin compatibility via [Nagios wrapper for agent plugin](https://pandorafms.com/library/nagios-wrapper-for-agent-plugin/)

- [Sensu](https://sensuapp.org/) - open-core distributed monitoring system, compatible with both Nagios and Zabbix plugins. Enterprise Edition contains metrics graphing integrations for [Graphite](https://sensuapp.org/docs/1.2/enterprise/integrations/graphite.html), [InfluxDB](https://sensuapp.org/docs/1.2/enterprise/integrations/influxdb.html) or [OpenTSDB](https://sensuapp.org/docs/1.2/enterprise/integrations/opentsdb.html) to graph the plugins' metrics perfdata

- [Check_MK](http://mathias-kettner.com/check_mk.html) - open-core Nagios-based monitoring solution with rule-based configuration, service discovery and agent-based multi-checks integrating [MRPE - MK's Remote Plugin Executor](https://mathias-kettner.de/checkmk_mrpe.html). See `adapter_check_mk.py` which can run any Nagios Plugin and convert its output to Check_MK local check format. Has built-in metrics graphing via [PNP4Nagios](http://docs.pnp4nagios.org/start), Enterprise Edition can send metrics to [Graphite](https://graphiteapp.org/) and [InfluxDB](https://www.influxdata.com/) via the Graphite protocol, see [documentation](https://mathias-kettner.com/cms_graphing.html)

- [ZenOSS](https://www.zenoss.com/) - open-core monitoring solution that can run Nagios Plugins, see [documentation](http://wiki.zenoss.org/Working_With_Nagios_Plugins)

- [OpsView Monitor](https://www.opsview.com/) - commercial Nagios-based monitoring distribution with native metrics graphing via [Graph Center](https://www.opsview.com/products/features/graph-center) as well as [InfluxDB integration](https://www.opsview.com/integrations/database/influxdb) via [InfluxDB Opspack](https://github.com/opsview/application-influxdb)

- [OP5 Monitor](https://www.op5.com/op5-monitor/) - commercial Nagios-based monitoring distribution including metrics graphing via [PNP4Nagios](http://docs.pnp4nagios.org/start), has [InfluxDB integration](https://kb.op5.com/display/HOWTOs/Install+OP5+Monitor+InfluxDB+module)

- [GroundWork Monitor](http://www.gwos.com/) - commercial Nagios-based monitoring distribution with RRD metrics graphing and [InfluxDB integration](https://kb.groundworkopensource.com/display/DOC72/How+to+configure+GroundWork+InfluxDB)

- [Geneos](https://www.itrsgroup.com/products/geneos) - proprietary non-standard monitoring, was used by a couple of banks I worked for. Geneos does not follow Nagios standards so integration is provided via `adapter_geneos.py` which if preprended to any standard nagios plugin command will execute and translate the results to the CSV format that Geneos expects, so Geneos can utilize any Nagios Plugin using this program

- [SolarWinds](https://www.solarwinds.com/) - proprietary monitoring solution but can take Nagios Plugins, see [doc](http://www.solarwinds.com/documentation/en/flarehelp/sam/content/SAM-Nagios-Script-Monitor-sw3266.htm)

- [Microsoft SCOM](https://www.microsoft.com/en-us/cloud-platform/system-center) - Microsoft Systems Center Operations Manager, can run Nagios Plugins as arbitrary Unix shell scripts with health / warning / error expression checks, see the [Microsoft technet documentation](https://technet.microsoft.com/en-us/library/jj126087(v=sc.12).aspx)

#### Incompatible Monitoring Solutions

- [Zabbix](https://www.zabbix.com/) - open source monitoring solution with in-built graphing, distributed monitoring and auto discovery but unfortunately not Nagios Plugin compatible, some integration can be done via a wrapper script (we tried exactly this in 2012 but didn't like it enough to switch from Nagios), see this [community forum thread](https://www.zabbix.com/forum/showthread.php?t=28010) for more information and code

- [OpsGenie](https://www.opsgenie.com/) - proprietary non-standard monitoring, cannot execute Nagios Plugins but has integration with existing [Nagios](https://docs.opsgenie.com/docs/nagios-overview), [Icinga2](https://docs.opsgenie.com/docs/icinga2-integration) and [Prometheus](https://docs.opsgenie.com/docs/prometheus-integration)

### Metrics Graphing Integrations

#### Graphite, InfluxDB, Prometheus, OpenTSDB, PNP4Nagios

Many monitoring systems will already auto-graph the performance metric data from these nagios plugins via [PNP4Nagios](http://docs.pnp4nagios.org/start) but you can also forward it to newer more specialised metrics monitoring and graphing systems such as [Graphite](https://graphiteapp.org/), [InfluxDB](https://www.influxdata.com/), [OpenTSDB](http://opentsdb.net/) and [Prometheus](https://prometheus.io/) (this last one is the most awkward as it requires pull rather than passively receiving).

The above list of [enterprise monitoring systems](nholuongut/nagios-nholuongut/nagios-pluginsing-systems) documents each one's integration capabilities with links to their documentation.

##### Metrics Collection Integrations

You can also execute these Nagios Plugins outside of any nagios-compatible monitoring server and forward just the metrics to the major metrics monitoring systems using the following tools:

- [Collectd](https://collectd.org/index.shtml) - metrics collection daemon - can execute Nagios Plugins to collect their perfdata via the [exec plugin](https://collectd.org/documentation/manpages/collectd-exec.5.shtml). Can send metrics to [Graphite](https://graphiteapp.org/), [InfluxDB](https://www.influxdata.com/) (via Graphite protocol), [Prometheus](https://prometheus.io/) (via exporter for scrape target) and [OpenTSDB](http://opentsdb.net/). See also the [collectd nagios plugin](https://collectd.org/documentation/manpages/collectd-nagios.1.shtml) which allows Nagios to query collectd metrics to apply alerts against them
- [Telegraf](https://docs.influxdata.com/telegraf/) - metrics collection daemon - can execute Nagios Plugins via `input.exec` with `data_format="nagios"` and pass the Nagios Plugin perfdata to [InfluxDB](https://www.influxdata.com/), [Graphite](https://graphiteapp.org/), [Prometheus](https://prometheus.io/) and [OpenTSDB](http://opentsdb.net/) - see the [InfluxDB data input formats documentation](https://github.com/influxdata/telegraf/blob/master/docs/DATA_FORMATS_INPUT.md#nagios)

##### Other Metrics Integration Add-Ons

- [PNP4Nagios](http://docs.pnp4nagios.org/start) - widely used open source auto-graphing add-on for Nagios open source and similar Nagios-based monitoring systems, see list of [enterprise monitoring systems](nholuongut/nagios-nholuongut/nagios-pluginsing-systems) above to see which ones bundle this
- [Graphios](https://github.com/shawn-sterling/graphios) - sends perfdata collected by Nagios to metrics graphing systems like [Graphite](https://graphiteapp.org/) or [InfluxDB](https://www.influxdata.com/) (via Graphite protocol)

###### Antiquated Monitoring Solutions You Probably Shouldn't Still Be Using Today

- [Cacti](https://www.cacti.net/)
- [Ganglia](http://ganglia.sourceforge.net/)
- [Munin](http://munin-monitoring.org/)
- [Mon](https://sourceforge.net/projects/mon/)
- [HP OpenView / BTO](https://en.wikipedia.org/wiki/HP_OpenView)
- [IBM Tivoli](https://www.ibm.com/developerworks/community/wikis/home?lang=en#!/wiki/Tivoli+Monitoring)

etc...

You may also be interested in the feature matrix on the [Wikipedia page - Comparison of network monitoring systems](https://en.wikipedia.org/wiki/Comparison_of_network_monitoring_systems).

### More 3rd Party Nagios Plugins

This is a list of the best and most interesting 3rd party plugins, several of which I have used or come across over the years that deserve mention, usually due to their better quality than the typical Nagios Exchange / Monitoring Exchange plugins.

- [check_openmanage](http://folk.uio.no/trondham/software/check_openmanage.html) - Dell PowerEdge servers hardware monitoring plugin using Dell OpenManage. Written by Trond Hasle Amundsen - checks RAID, Processors, Memory, Fans, Temperature, Power Supplies etc. Top quality widely used plugin - one of my all time favourites
- [Consol Labs](https://labs.consol.de/) checks - one of the very best quality publishers of Nagios Plugins (I have a lot of respect for this team):
  - [check_hpasm](https://labs.consol.de/nagios/check_hpasm/index.html) - HP Proliant servers hardware monitoring plugin using ASM - checks RAID, Processors, Memory, Fans, Temperature, Power supplies
  - [check_logfiles](https://labs.consol.de/nagios/check_logfiles/index.html) - the best log monitoring Nagios Plugin I've seen, even accounts for log rotations
  - [check_webinject](https://labs.consol.de/nagios/check_webinject/index.html) - see below
- [WebInject](http://www.webinject.org/plugin.html) - authenticate through HTTP Login portals and check the inside. Widely used and flexible via external XML config. Excellent  - I used to use this a lot and it's probably the best of it's kind
- [Jolokia](https://jolokia.org/) - JMX-HTTP bridge to make monitoring JMX easier via Rest calls from non-JVM scripting languages. This is far more scalable than running lots of JVM Nagios Plugins which have higher startup overhead
  - [check_jmx4perl](https://exchange.nagios.org/directory/Plugins/Java-Applications-and-Servers/check_jmx4perl/details) - use with Jolokia
- [Percona plugins](https://www.percona.com/doc/percona-monitoring-plugins/latest/index.html) - MySQL plugins from MySQL specialists
- [check_drbd](https://exchange.nagios.org/directory/Plugins/Operating-Systems/Linux/check_drbd/details) - can't remember if this is the DRBD plugin I used to use, but iirc it was good at tracking lag on secondary and catch-up
- [check_tsd](https://github.com/OpenTSDB/opentsdb/blob/master/tools/check_tsd) - OpenTSDB metrics query
- [check_prometheus_metric.sh](https://github.com/prometheus/nagios_plugins/blob/master/checks/check_prometheus_metric.sh) - I don't normally rate bash scripts as Nagios Plugins but this is in the official project so it's worth a look
- [collectd-nagios](https://collectd.org/documentation/manpages/collectd-nagios.1.shtml) - queries Collectd metrics for Nagios alerting
- [collectd exec-nagios.px](https://github.com/collectd/collectd/blob/master/contrib/exec-nagios.px) - executes a Nagios Plugin and returns the metrics to Collectd to forward on to one of the many compatible metrics graphing solutions
- [Datameer](https://www.datameer.com) references this project in the [Datameer docs](https://www.datameer.com/documentation/current/Monitoring+Hadoop+and+Datameer+using+Nagios) from version 3 onwards. Datameer wrote 1 example nagios plugin on that page, then referenced the 9 additional plugins here in the links section at the bottom along with the official Nagios links

# 🚀 I'm are always open to your feedback.  Please contact as bellow information:
### [Contact ]
* [Name: nho Luong]
* [Skype](luongutnho_skype)
* [Github](https://github.com/nholuongut/)
* [Linkedin](https://www.linkedin.com/in/nholuong/)
* [Email Address](luongutnho@hotmail.com)
* [PayPal.me](https://www.paypal.com/paypalme/nholuongut)

![](https://i.imgur.com/waxVImv.png)
![](Donate.png)
[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/nholuong)

# License
* Nho Luong (c). All Rights Reserved.🌟