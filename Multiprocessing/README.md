<body>
  <h2>Multiprocessing</h2>  
  <p>Multiprocessing refers to the ability of a system to support more than one processor at the same time. Applications in a multiprocessing system are broken to smaller routines that run independently. The operating system allocates these threads to the processors improving performance of the system.</p>
  <ul>
  <li>we use os.getpid() function to get ID of process running the current target function.</li>
  <li>Each process runs independently and has its own memory space.</li>
   <li>we use p1.is_alive() method of Process class to check if a process is still active or not.</li>
 </body>
