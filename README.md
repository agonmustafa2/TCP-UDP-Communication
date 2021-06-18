# TCP-UDP-Communication

   Qëllimi i këtij projekti është dizajnimi, implementimi dhe testimi i dy programeve, serveri dhe klienti,
 dhe komunikimi mes tyre përmes protokollove.Klienti është ai që kërkon shërbime prej serverit, dhe kjo është
 ilustruar me definimin e disa metodave në server, për të cilat ky i fundit mund të jap përgjigje në varësi të 
 vlerave hyrëse që jipen nga klienti.Transmission Control Protocol/Internet Protocol (TCP/IP) u bë protokoll 
 standard në vitin 1982, i cili mundëson që një program në një kompjuter të komunikojë përmes Internetit  
 me një program në kompjuter tjetër. TCP/IP ofron ndërfaqe të nivelit të ulët që i mundëson kompjuterëve 
 (dhe paisjeve tjera të ndryshme tërësishtë mes vete) të lidhur në Internet të duken saktësishte  njësoj.
      TCP është protokoll që ofron transport të besueshëm, të rregullt dhe të kontrolluar për gabime në transmetim.
      UDP (User Datagram Protocol) është protokoll që për dallim nga protokolli TCP nuk ofron transport të besueshëm,
 të rregullt dhe të kontrolluar për gabime në transmetim.UDP funksionon pa konektim, d.m.th. nuk ka handshaking 
 para se të fillojë komunikimi. Ky protokoll nuk garanton nëse mesazhi do të merret. Për më tepër, ato mesazhe 
 që arrijnë gjatë procesit të marrjes mund të jenë jo të renditura.
 Në dy protokollet (TCP dhe UDP) është përdorur programimi me soketa (Sockets Programming), në gjuhën programuese Python.
 Libraria standarde Python ka një modul të quajtur socket. Disa nga metodat më të rëndësishme qe gjenden në këtë modul 
 dhe janë përdorur për realizim të projektit janë: bind(), listen(), accept(), connect(), send(), recv() etj.
