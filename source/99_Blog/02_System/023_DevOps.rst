==============================================
获取锁及打开表会话的脚本
==============================================

获取锁
---------------------

脚本文件：``getLockTab.sh``  

.. code:: shell

  #!/bin/bash
  # filename: getLockTab.sh
  # function: get sessions for table which locked.
  # write by: liaosnet@gbasedbt.com  2022-03-15

  if [ ! $# -eq 2 ]; then
    cat << EOF 2>/dev/null
  
    Usage: getLockTab.sh DBNAME TABNAME
  
  EOF
    exit 1
  fi

  DBNAME=$(echo $1 | tr '[A-Z]' '[a-z]')
  TABNAME=$(echo $2 | tr '[A-Z]' '[a-z]')

  SESID=$(dbaccess sysmaster - << !SQL 2>/dev/null
  set isolation to dirty read;
  select owner as sesid
  from syslocks
  where dbsname = '${DBNAME}'
    and tabname = '${TABNAME}'
    group by owner;
  !SQL
  )

  echo $SESID

  exit 0


获取打开表
--------------  
脚本文件： ``getOpenTab.sh``  

.. code:: shell

  #!/bin/bash
  # filename: getOpenTab.sh
  # function: get sessions for table which opened.
  # write by: liaosnet@gbasedbt.com  2023-08-14
  export LANG=C
  loginfo(){
    echo -e "[$(date +'%Y-%m-%d %H:%M:%S')] $*"
  }

  if [ ! $# -eq 2 ]; then
    cat << EOF 2>/dev/null
  
    Usage: getOpenTab.sh DBNAME TABNAME
  
  EOF
    exit 1
  fi

  DBNAME=$(echo $1 | tr '[A-Z]' '[a-z]')
  TABNAME=$(echo $2 | tr '[A-Z]' '[a-z]')

  # get partnum
  PTNFILE="_TMP_PTNFILE"
  dbaccess ${DBNAME} - <<! >/dev/null 2>&1
  -- normal table
  unload to ${PTNFILE}.normal delimiter ' '
  select ltrim(lower(hex(partnum)),'0x') partnum 
    from systables 
   where tabname = '${TABNAME}';
  -- fragment / partition tables
  unload to ${PTNFILE}.frag delimiter ' '
  select ltrim(lower(hex(f.partn)),'0x') partnum 
    from sysfragments f, systables t
   where f.tabid = t.tabid
     and f.fragtype = 'T'
     and t.tabname = '${TABNAME}';
  !
  
  cat /dev/null > ${PTNFILE}
  if [ -f ${PTNFILE}.normal ]; then
    cat ${PTNFILE}.normal > ${PTNFILE}
    rm -f ${PTNFILE}.normal
  fi
  
  if [ -f ${PTNFILE}.frag ]; then 
    cat ${PTNFILE}.frag >> ${PTNFILE}
    rm -f ${PTNFILE}.frag
  fi
  
  if [ -s ${PTNFILE} ]; then
    sed -i '/^\\.*$/d' ${PTNFILE}
  fi
  
  #
  OPNFILE="_TMP_OPNFILE"
  TIDFILE="_TMP_OPNTIDF"
  SES0FILE="_TMP_SES0FILE"
  onstat -g opn > ${OPNFILE}
  onstat -g ses 0 > ${SES0FILE}
  if [ -s ${OPNFILE} ]; then
    while read PARTNUM
    do
      if [ ! x"${PARTNUM}" = x ]; then
        awk -v partn="${PARTNUM}" '
          /^rstcb/ || /^$/ {rs=1};
          /^isfd/{rs=0};
          rs==1{if(lktab==1)print op; lktab=0; op=$0};
          rs==0 && $4=="0x"partn{lktab=1}
        ' ${OPNFILE} > ${TIDFILE}
      fi 
    done < ${PTNFILE}
  fi

  if [ -s ${TIDFILE} ]; then
    while read _RSTCB RSTCB _TID TID
    do
      # echo ${RSTCB:2} $TID
      awk -v rstcb="${RSTCB:2}" -v rstid="${TID}" '
        /^session/{need=1;getline;getline;sid=$1}
        /^tid/ && need==1 {getline;if(rstid==$1 && rstcb==$3){sesid=sesid" "sid}}
        END{print "sesid"sesid}' ${SES0FILE}
    done < ${TIDFILE}
  fi

  if [ -f ${TIDFILE} ]; then
    rm -f ${TIDFILE}
  fi

  if [ -f ${SES0FILE} ]; then
    rm -f ${SES0FILE}
  fi

  if [ -f ${OPNFILE} ]; then
    rm -f ${OPNFILE}
  fi

  if [ -f ${PTNFILE} ]; then
    rm -f ${PTNFILE}
  fi
  
  exit 0

最后更新日期：2025-11-19
