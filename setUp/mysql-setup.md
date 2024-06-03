* Oracle-Mysql download site: https://dev.mysql.com/downloads/windows/installer/8.0.html  
![image](https://user-images.githubusercontent.com/22329486/221425302-ae36fa48-79d2-4625-9c39-3ff6ea4cdf8f.png)  
![image](https://user-images.githubusercontent.com/22329486/221425339-57880361-4d1c-4595-b18a-f5652ee9ef80.png)  

Open the Services Management Console:  
1. Press Windows + R.  
Type services.msc and press Enter.  
Locate and Start the MySQL Service:  

2. Find the MySQL service in the list (e.g., MySQL80).  
Right-click on the service and select Start.  
![image](https://github.com/GinChoYen/Anthony/assets/22329486/8807ad55-ab33-48ae-b9a5-aff30d901896)  

3. install paht C:\Program Files\MySQL  
![image](https://github.com/GinChoYen/Anthony/assets/22329486/4031fa51-d76f-4c11-9b6b-e4710b03e6c1)
Install the MySQL Service:  
  * Run the following command to install the MySQL service:  
C:\Program Files\MySQL\MySQL Server 8.0\bin\mysqld --install
![image](https://github.com/GinChoYen/Anthony/assets/22329486/fc49b95c-9361-4c24-8bdf-ece1c08d4c78)  
  * Start the MySQL Service:  
Start the service using:  net start MySQL80 or use services.msc  

