CREATE TABLE INDIA_TEAM_A(
  PLAYER_NUM INT,
  PLAYER_NAME CHAR(10),
  PLAYER_BOWLING_SPEED INT,
  PLAYER_ROLE VARCHAR(30),
  PLAYER_AVERAGE DECIMAL(4,1),
  PLAYER_SALARY VARCHAR(10),
  PLAYER_ADDS VARCHAR(50),
  PLAYER_LINEUP INT,
  PLAYER_FOLLOWERS VARCHAR(10),
  PLAYER_MARTIAL_STATUS CHAR(3)
);

INSERT INTO INDIA_TEAM_A VALUES(7,'DHONI',0,'BATSMAN AND CAPTAIN',50.8,'3CR','BOOST',6,'40M','M');
INSERT INTO INDIA_TEAM_A VALUES(10,'ROHIT',0,'BATSMAN AND VICE CAPTAIN',80.8,'3CR','CEAT',1,'50M','M');
INSERT INTO INDIA_TEAM_A VALUES(18,'VIRAT',0,'BATSMAN',95.8,'3CR','MRF',3,'240M','M');
INSERT INTO INDIA_TEAM_A VALUES(11,'SANJU',0,'BATSMAN',80.8,'3CR','DREAM 11',5,'40M','M');
INSERT INTO INDIA_TEAM_A VALUES(8,'PANDIYA',140,'ALLROUNDER',50.8,'3CR','DREAM 11',4,'80M','D');
INSERT INTO INDIA_TEAM_A VALUES(12,'GILL',0,'BATSMAN',70.8,'2CR','BOOST',5,'40M','S');
INSERT INTO INDIA_TEAM_A VALUES(62,'BUMRAH',153,'BOWLER',0.0,'3CR','BALL',5,'40M','M');
INSERT INTO INDIA_TEAM_A VALUES(34,'SHAMI',150,'BOWLER',0.0,'3CR','DREAM 11',5,'12M','M');
INSERT INTO INDIA_TEAM_A VALUES(23,'SIRAJ',150,'BOWLER',10.0,'3CR','BYJUS',5,'25M','M');

SELECT * FROM INDIA_TEAM_A;

Output
PLAYER_NUM	PLAYER_NAME	PLAYER_BOWLING_SPEED	PLAYER_ROLE	PLAYER_AVERAGE	PLAYER_SALARY	PLAYER_ADDS	PLAYER_LINEUP	PLAYER_FOLLOWERS	PLAYER_MARTIAL_STATUS
7	DHONI	0	BATSMAN AND CAPTAIN	50.8	3CR	BOOST	6	40M	M
10	ROHIT	0	BATSMAN AND VICE CAPTAIN	80.8	3CR	CEAT	1	50M	M
18	VIRAT	0	BATSMAN	95.8	3CR	MRF	3	240M	M
11	SANJU	0	BATSMAN	80.8	3CR	DREAM 11	5	40M	M
8	PANDIYA	140	ALLROUNDER	50.8	3CR	DREAM 11	4	80M	D
12	GILL	0	BATSMAN	70.8	2CR	BOOST	5	40M	S
62	BUMRAH	153	BOWLER	0.0	3CR	BALL	5	40M	M
34	SHAMI	150	BOWLER	0.0	3CR	DREAM 11	5	12M	M
23	SIRAJ	150	BOWLER	10.0	3CR	BYJUS	


--UPDATE 

UPDATE INDIA_TEAM_A
SET PLAYER_BOWLING_SPEED = 160
WHERE PLAYER_NUM = 62;

| PLAYER_NUM | PLAYER_NAME | PLAYER_BOWLING_SPEED |
| ---------: | ----------- | -------------------: |
|         62 | BUMRAH      |                  160 |

--DELETE 
DELETE INDIA_TEAM_A
WHERE PLAYER_NUM = 18;

| PLAYER_NUM | PLAYER_NAME | PLAYER_ROLE              |
| ---------: | ----------- | ------------------------ |
|          7 | DHONI       | BATSMAN AND CAPTAIN      |
|         10 | ROHIT       | BATSMAN AND VICE CAPTAIN |
|         11 | SANJU       | BATSMAN                  |
|          8 | PANDIYA     | ALLROUNDER               |
|         12 | GILL        | BATSMAN                  |
|         62 | BUMRAH      | BOWLER                   |
|         34 | SHAMI       | BOWLER                   |
|         23 | SIRAJ       | BOWLER                   |


--ALTER 

ALTER TABLE INDIA_TEAM_A
ADD COLUMN PLAYER_RATINGS INT;

| Column Name           | Data Type    |
| --------------------- | ------------ |
| PLAYER_NUM            | INT          |
| PLAYER_NAME           | CHAR(10)     |
| PLAYER_BOWLING_SPEED  | INT          |
| PLAYER_ROLE           | VARCHAR(30)  |
| PLAYER_AVERAGE        | DECIMAL(4,1) |
| PLAYER_SALARY         | VARCHAR(10)  |
| PLAYER_ADDS           | VARCHAR(50)  |
| PLAYER_LINEUP         | INT          |
| PLAYER_FOLLOWERS      | VARCHAR(10)  |
| PLAYER_MARTIAL_STATUS | CHAR(3)      |
| **PLAYER_RATINGS**    | **INT**      |

--RENAME 

ALTER TABLE INDIA_TEAM_A
RENAME COLUMN PLAYER_MARTIAL_STATUS TO PLAYER_MS;



| Column Name          | Data Type    |
| -------------------- | ------------ |
| PLAYER_NUM           | INT          |
| PLAYER_NAME          | CHAR(10)     |
| PLAYER_BOWLING_SPEED | INT          |
| PLAYER_ROLE          | VARCHAR(30)  |
| PLAYER_AVERAGE       | DECIMAL(4,1) |
| PLAYER_SALARY        | VARCHAR(10)  |
| PLAYER_ADDS          | VARCHAR(50)  |
| PLAYER_LINEUP        | INT          |
| PLAYER_FOLLOWERS     | VARCHAR(10)  |
| **PLAYER_MS**        | CHAR(3)      |


--DISTINCT KEY

SELECT DISTINCT *
FROM INDIA_TEAM_A;


| PLAYER_ROLE              |
| ------------------------ |
| BATSMAN AND CAPTAIN      |
| BATSMAN AND VICE CAPTAIN |
| BATSMAN                  |
| ALLROUNDER               |
| BOWLER                   |

--WHERE CONDITION

SELECT PLAYER_SALARY
FROM INDIA_TEAM_A
WHERE PLAYER_SALARY >= '3CR';

| PLAYER_SALARY |
| ------------- |
| 3CR           |
| 3CR           |
| 3CR           |
| 3CR           |
| 3CR           |
| 3CR           |
| 3CR           |
| 3CR           |


--ORDER BY 

SELECT PLAYER_NUM
FROM INDIA_TEAM_A
ORDER BY PLAYER_NUM ASC;

| PLAYER_NUM |
| ---------: |
|          7 |
|          8 |
|         10 |
|         11 |
|         12 |
|         18 |
|         23 |
|         34 |
|         62 |

--LIMIT

SELECT PLAYER_NUM 
FROM INDIA_TEAM_A
LIMIT 3;

| PLAYER_NUM |
| ---------: |
|          7 |
|         10 |
|         18 |

SELECT PLAYER_NUM
FROM INDIA_TEAM_A
WHERE PLAYER_NUM <= 60;

| PLAYER_NUM |
| ---------: |
|          7 |
|         10 |
|         18 |
|         11 |
|          8 |
|         12 |
|         34 |
|         23 |

SELECT PLAYER_NUM,PLAYER_ROLE
FROM INDIA_TEAM_A
WHERE PLAYER_NUM <= 60
AND PLAYER_ROLE = 'BATTING';

| PLAYER_NUM | PLAYER_ROLE              |
| ---------: | ------------------------ |
|          7 | BATSMAN AND CAPTAIN      |
|         10 | BATSMAN AND VICE CAPTAIN |
|         18 | BATSMAN                  |
|         11 | BATSMAN                  |
|         12 | BATSMAN                  |

SELECT PLAYER_NUM,PLAYER_ROLE
FROM INDIA_TEAM_A
WHERE PLAYER_NUM <= 60 
OR PLAYER_ROLE = 'ALLROUNDER';

--CONDITION 1

| PLAYER_NUM |
| ---------: |
|          7 |
|         10 |
|         18 |
|         11 |
|          8 |
|         12 |
|         34 |
|         23 |

--CONDITION 2

| PLAYER_NUM | PLAYER_ROLE |
| ---------: | ----------- |
|          8 | ALLROUNDER  |

--MAX() -AGGREGATE 

SELECT MAX (PLAYER_AVERAGE)
FROM INDIA_TEAM_A;

| MAX(PLAYER_AVERAGE) |
| ------------------: |
|                95.8 |

SELECT SUM(PLAYER_AVERAGE)
FROM INDIA_TEAM_A;

50.8 + 80.8 + 95.8 + 80.8 + 50.8 + 70.8 + 0.0 + 0.0 + 10.0
= 439.8

--IN

SELECT *
FROM INDIA_TEAM_A
WHERE PLAYER_ROLE IN ('BOWLER', 'ALLROUNDER');

| PLAYER_NUM | PLAYER_NAME | PLAYER_BOWLING_SPEED | PLAYER_ROLE | PLAYER_AVERAGE |
| ---------: | ----------- | -------------------: | ----------- | -------------: |
|          8 | PANDIYA     |                  140 | ALLROUNDER  |           50.8 |
|         62 | BUMRAH      |                  153 | BOWLER      |            0.0 |
|         34 | SHAMI       |                  150 | BOWLER      |            0.0 |
|         23 | SIRAJ       |                  150 | BOWLER      |           10.0 |

--NOT IN

SELECT *
FROM INDIA_TEAM_A
WHERE PLAYER_ROLE NOT IN ('BOWLER', 'ALLROUNDER');

| PLAYER_NUM | PLAYER_NAME | PLAYER_ROLE              |
| ---------: | ----------- | ------------------------ |
|          7 | DHONI       | BATSMAN AND CAPTAIN      |
|         10 | ROHIT       | BATSMAN AND VICE CAPTAIN |
|         18 | VIRAT       | BATSMAN                  |
|         11 | SANJU       | BATSMAN                  |
|         12 | GILL        | BATSMAN                  |

--BETWEEN 

SELECT *
FROM INDIA_TEAM_A
WHERE PLAYER_AVERAGE BETWEEN 60 AND 90;

| PLAYER_NUM | PLAYER_NAME | PLAYER_AVERAGE | PLAYER_ROLE              |
| ---------: | ----------- | -------------: | ------------------------ |
|         10 | ROHIT       |           80.8 | BATSMAN AND VICE CAPTAIN |
|         11 | SANJU       |           80.8 | BATSMAN                  |
|         12 | GILL        |           70.8 | BATSMAN                  |

SELECT COUNT(*)
FROM INDIA_TEAM_A;

| COUNT(*) |
| -------: |
|        9 |




