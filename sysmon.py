ó
øhØ^c           @   s  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d d d  Z e	 d  Z
 d   Z d   Z d   Z d	   Z d
   Z d   Z d   Z e d k re  j d d d d d e  j  Z e j d d d e d e d d d d e j d d d e d e d d d d e j d d  d e d e d d! d d" e j d# d$ d% d& d e d e d g  d d' e j d( d) d% d& d e d e d g  d d* e j d+ d, d e d e d d- d d. e j   Z e j Z e j Z e j Z  e j! Z! e j Z" e j# Z$ e j% Z& e a' e j e j( e  e j e j) e  e j e j* e  e e e! e  e" e$ e&  n  d S(/   iÿÿÿÿNi
   i    c         C   s»  i  } t  |   } d } x¨ |  D]  } t  |  } | | } t | |  }	 g  t d t  |  |  D] }
 | |
 |
 | !^ qd } | d k r |	 d }	 n  t | |  } | |	 | | f | | <q W| | } | | } | d k rð | d } n  | } x­ | d k r¥d } xw |  D]o } | | d | k rmt  | | d  d k rmd | | | | d j d  f } qd | d | f } qWd | | } | GH| d } qù Wd | d | GHd	 S(
   s¤   
	æ é¢ååå½æ°ï¼ è®©æ é¢çæ¯åé¿åº¦æ ¹æ®æå®çå®½åº¦æ¢è¡
	:param titlelist:æ é¢åè¡¨[]
	:param width:åå®½åº¦
	:param preBlank:åç¼ç©ºæ ¼
	i    i   t    i   s   %s%-*s s   %s%s t    t   -N(   t   lent   intt   ranget   maxt   pop(   t	   titlelistt   widtht   preBlankt	   titleinfot   titlelistLent	   maxlengtht   onetitlet   lengtht	   remaindert   multiplet   it   onetitleCutt   maxRemaindert   maxMultiplet   lineNumt   oneLine(    (    s	   sysmon.pyt   titlecut   s6    
6

.'c      	   C   sC   | r t  j |  d t }  n! t  j |  d t d d d d }  |  S(   Nt   ensure_asciit   indenti   t
   separatorst   ,t   :(   R   R   (   t   jsont   dumpst   False(   t   msgt   simple(    (    s	   sysmon.pyt   toJson2   s    !c          C   sÇ   t  j d  }  |  j   } |  j   t | j   j d  j    } t | d  t | d  t | d  t | d  t | d  t | d  t | d	  } | | d
 <t t |  } | S(   Ns   grep -i ^cpu /proc/stat|head -1s   
i   i   i   i   i   i   i   i    (	   t   ost   popent   readlinet   closet   listt   stript   splitR   t   map(   t   cpuPopent   cpudatat   cpulistt   cputotal(    (    s	   sysmon.pyt   getCpu:   s    
!d
c          C   sY   t  j d  }  |  j   } |  j   t | j   j d  j    } t t |  } | S(   NsK   grep -E 'pswpin|pswpout|pgpgin|pgpgout' /proc/vmstat|awk '{print $2}'|xargss   
(	   R$   R%   R&   R'   R(   R)   R*   R+   R   (   t	   swapPopent   swapdatat   swaplist(    (    s	   sysmon.pyt   getSwapF   s    
!c          C   sÞ   t  j d  }  |  j   } i  } x¶ | D]® } t | j   j d  j    } | j d  j   j d  } t t |  } | | | <| j	 d  s¢ | | d <q( g  t
 | d |  D] \ } } | | ^ q¶ | d <q( W| S(   Ns+   grep -viE 'lo:|packets|Inter' /proc/net/devs   
i    R   t   all(   R$   R%   t	   readlinesR(   R)   R*   R   R+   R   t   has_keyt   zip(   t   netPopent   netdatat   netdictt   onet   netlistt   netNameR   t   j(    (    s	   sysmon.pyt   getNetP   s    !
8c          C   sò   t  j d  }  |  j   } i  } xÊ | D]Â } t | j   j d  j    } | d =| d =| j d  } t t |  } | | | <t	 j
 d |  r( | j d  s³ | | d <qê g  t | d |  D] \ } } | | ^ qÇ | d <q( q( W| S(   Ns$   grep -ivE 'ram|loop' /proc/diskstatss   
i    s   .*[a-z]$R5   (   R$   R%   R6   R(   R)   R*   R   R+   R   t   ret   matchR7   R8   (   t	   diskPopent   diskdatat   diskdictR<   t   disklistt   diskNameR   R?   (    (    s	   sysmon.pyt   getDisk`   s    !
;c          C   sH   t  j d  }  |  j   } | j   j d  j   } | d =| d =| S(   Ns   cat /proc/loadavgs   
iÿÿÿÿ(   R$   R%   R&   R)   R*   (   t	   loadPopent   loaddatat   loadlist(    (    s	   sysmon.pyt   getLoads   s    c   4      C   sº  yd d d d d d d d d	 d
 d g } t  j |  } d d d d d d d g } d d d d d d g }	 t   }
 t   } t   } t   } t   } t t |   } t t |   } xN | D]F } | j	 |  rÄ x. | D]# } d | | f } | j
 |  qà WqÄ qÄ WxN | D]F } | j	 |  rx. |	 D]# } d | | f } | j
 |  q1WqqWt t  j   j   } | d k rt j d  } n t j d | t j  } g  } x3 | D]+ } | j |  d; k	 r»| j
 |  q»q»W| } | j
 d  t j d  d } xt rt r/t j d  n  | | d k rOt | |  n  t   } t   } t   } t   } t   } t j d   } t | d | d  } i | d d 6| d d 6| d! d 6} i t d" | d | d | d  d 6t d" | d# | d# | d  d 6t d" | d$ | d$ | d  d 6t d" | d% | d% | d  d 6} i t | d | d |   d 6t | d | d |   d	 6t | d! | d! |   d
 6t | d# | d# |   d 6}  i  }! |! j |  |! j |  |! j |   i  }" x| D]} t | | d | | d  }# t |# |   }$ t | | d$ | | d$  }% t |% |   }& t | | d! | | d! |  d!  }' t | | d& | | d& |  d!  }( | | d' }) t | | d# | | d# t  |# d  d  }* t | | d( | | d( t  |% d  d  }+ |$ |" d) | <|& |" d* | <|' |" d+ | <|( |" d, | <|) |" d- | <|* |" d. | <|+ |" d/ | <qW|! j |"  i  }, xJ| D]B} t | | d | | d  |  d' d0 }- t | | d | | d |   }. t | | d# | | d# |   }/ t | | d' | | d'  |  d' d0 }0 t | | d1 | | d1  |  }1 t | | d2 | | d2  |  }2 |- |, d3 | <|. |, d4 | <|/ |, d5 | <|0 |, d6 | <|1 |, d7 | <|2 |, d8 | <q¸W|! j |,  | |! d <x, | D]$ } t! j" j# d9 | |! | f  qWt! j" j# d:  t! j" j$   | }
 | } | } | } | } | d } t j |   qWWn t% k
 rµ}3 |3 GHn Xd; S(<   sä   
	è¾åºå¹éçç³»ç»æ§è½å¼
	:param interval: é´éæ¶é´
	:param width: åå®½
	:param header: æ é¢æå°é¢æ¬¡
	:param matchstr: å¹éæ é¢
	:param devicelist: ç¡¬çè®¾å¤åè¡¨
	:param netlist: ç½ç»æ¥å£åè¡¨
	s   load.1ms   load.5ms   load.15ms   cpu.usrs   cpu.syss   cpu.idles
   cpu.iowaits   page.ins   page.outs   swap.ins   swap.outs   r/ss   w/ss   rkB/ss   wkB/st   queuet   rwaitt   wwaits   netIn.KBt   inPackt   inDrops	   netOut.KBt   outPackt   OutDrops   %s.%sR    s   .*s   .*%s.*t   timei   i    s   %H:%M:%Si   id   i   i   i   i   i   i   s   %s.r/ss   %s.w/ss   %s.rkB/ss   %s.wkB/ss   %s.queues   %s.rwaits   %s.wwaiti   i	   i   s   %s.netIn.KBs	   %s.inPacks	   %s.inDrops   %s.netOut.KBs
   %s.outPacks
   %s.OutDrops   %-*s s   
N(&   t   copyt   deepcopyRL   R0   R4   RH   R@   R(   t   setR7   t   appendt   strt   strMatcht   lowerR)   RA   t   compilet
   IGNORECASEt   searcht   NoneRT   t   sleept   Truet   is_sigint_upR$   t   _exitR   t   strftimet   floatt   roundR   t   updateR   t   syst   stdoutt   writet   flusht	   Exception(4   t   intervalR	   t   headert   matchstrt
   devicelistR=   R.   t   titlet
   diskOptiont	   netOptiont   oldloadt   oldcput   oldswapt   olddiskt   oldnett	   oneDevicet	   oneOptionR   t   oneNett   strMatchLowert   pmt
   titleMatcht   countt   newloadt   newcput   newswapt   newdiskt   newnett
   currentimet   cpuTotalDifft   loadDifft   cpuDifft   swapDifft
   titleValuet   devicelistDifft	   readTimest   readrst   writerTimest   writerst   readkbst   writekbsRM   RN   RO   t   netlistDifft   netInt	   inPackaget	   netInDropt   netOutt
   outPackaget
   netOutDropt   error(    (    s	   sysmon.pyt   mainpro|   sÊ    
'											'z  ((00,$$,$$
"
c         C   s   t  a d GHd  S(   Ns   catched interrupt signal!(   Ra   Rb   (   t   signumt   frame(    (    s	   sysmon.pyt   sigint_handlerþ   s    t   __main__t   epilogs   by van 2020t   descriptions   *Linux system monitor tool*
t   formatter_classs   -is
   --intervalt   typet   requiredt   defaulti   t   helps   è¾åºæ¶é´é´é,é»è®¤1ç§s   -ws   --widthi   s   è¾åºå®½åº¦,é»è®¤6s   -ts   --titlei2   s0   æå°æ é¢,é»è®¤æ¯é50è¡æå°ä¸æ¬¡æ é¢s   -ds   --devicet   actionRX   s(   æå®ç£ç,æå®allè¡¨ç¤ºææç£çs   -ns   --nets(   æå®ç½å¡,æå®allè¡¨ç¤ºææç½å¡s   -ms   --matchR    s   å¹å¯¹è¾åºé¡¹(+   t   argparseRU   R   RA   t   signalR$   Rh   RT   R   Ra   R#   R0   R4   R@   RH   RL   R   R   t   __name__t   ArgumentParsert   RawTextHelpFormattert   parsert   add_argumentR   R    RY   t
   parse_argst   argsRB   RZ   Rm   Rq   Rn   R	   Ro   t   deviceRp   t   netR=   Rb   t   SIGINTt   SIGHUPt   SIGTERM(    (    (    s	   sysmon.pyt   <module>   sJ   &		
						!(((..(							