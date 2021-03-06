-- ----------------------------
-- Procedure structure for t4_cl
-- ----------------------------
DROP PROCEDURE IF EXISTS `t4_cl`;

DELIMITER //
CREATE DEFINER = `root`@`localhost`
PROCEDURE `t4_cl`()
BEGIN
    DECLARE s int default 0;
    #DECLARE t VARCHAR(300);  
    DECLARE cl int;
    DECLARE i int;
    DECLARE week1 int;
    DECLARE week2 int;
    DECLARE ser int;
    DECLARE p1 int;
    DECLARE p2 int;
    DECLARE p3 int;
    DECLARE p4 int;
    DECLARE p5 int;
    DECLARE n1 int;
    DECLARE n2 int;
    DECLARE n3 int;
    DECLARE n4 int;
    DECLARE n5 int;
    DECLARE up1 int;
    DECLARE up2 int;
    DECLARE up3 int;
    DECLARE up4 int;
    DECLARE up5 int;
    DECLARE un1 int;
    DECLARE un2 int;
    DECLARE un3 int;
    DECLARE un4 int;
    DECLARE un5 int;

    # ignore
    DECLARE items_ids TEXT;
    DECLARE item1_ids TEXT;
    DECLARE item2_ids TEXT;

    DECLARE cur CURSOR FOR 
    SELECT DISTINCT 
      #title 
      #industry_id
      career_level
    #FROM item LIMIT 1;
    FROM item;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET s = 1;

    OPEN cur;
    FETCH cur INTO cl;
    #SET dpl='2848370,1477425';
    WHILE s <> 1 DO
        #IF t <> '' THEN
        IF cl <> 0 THEN
            SET i = 35;
            while i <= 42 do
                SET week1 = i;
                SET week2 = i + 1;
                SET ser = i + 2;

                #
                SELECT IFNULL(COUNT(id), 0) INTO p1 
                FROM join_uia 
                WHERE ui_week = week1 
                AND interaction_type in (1, 2, 3)
                AND i_career_level = cl
                AND i_week = week1;

                #
                SELECT IFNULL(COUNT(id), 0) INTO p2 
                FROM join_uia 
                WHERE ui_week = week2 
                AND interaction_type in (1,2,3) 
                AND i_career_level = cl
                AND i_week = week1;

                #
                SELECT IFNULL(COUNT(id), 0) INTO p3 
                FROM join_uia 
                WHERE ui_week = week2 
                AND interaction_type in (1,2,3) 
                AND i_career_level = cl 
                AND i_week = week2;

                #
                SELECT IFNULL(COUNT(id),0) into n1 
                FROM join_uia 
                WHERE ui_week = week1 
                and interaction_type=4 
                and i_career_level = cl
                AND i_week = week1;

                #
                SELECT IFNULL(COUNT(id),0) into n2 
                FROM join_uia 
                WHERE ui_week = week2 
                AND interaction_type = 4 
                AND i_career_level = cl 
                AND i_week = week1;

                #
                SELECT IFNULL(COUNT(id),0) into n3 
                FROM join_uia 
                WHERE ui_week = week2 
                AND interaction_type=4 
                AND i_career_level = cl 
                AND i_week = week2;
                            
                UPDATE sample 
                #
                SET
                sj_cl_1_1_p=p3,sj_cl_1_1_n=n3,sj_cl_2_1_p=(p2+p3),sj_cl_2_1_n=(n2+n3),sj_cl_2_2_p=(p1+p2+p3),sj_cl_2_2_n=(n1+n2+n3)
                #
                WHERE i_career_level = cl 
                AND serial = ser;

                BEGIN
                    DECLARE ss int default 0;
                    DECLARE uid int;
                    DECLARE c int;

                    DECLARE cur2 CURSOR FOR 
                    SELECT 
                        user_id,
                        IFNULL(COUNT(id),0) 
                    FROM join_uia 
                    WHERE ui_week = week1 
                    AND interaction_type in (1,2,3) 
                    #
                    AND i_career_level = cl 
                    AND i_week = week1 
                    GROUP BY user_id;

                    DECLARE CONTINUE HANDLER FOR NOT FOUND SET ss = 1;
                    open cur2;

                    FETCH cur2 into uid, c;
                    WHILE ss <> 1 DO
                        UPDATE sample 
                        #
                        SET usj_cl_1_p = c  
                        #
                        WHERE i_career_level = cl 
                        AND serial = ser 
                        AND user_id = uid;
                        FETCH cur2 into uid, c;
                    END WHILE;

                    CLOSE cur2;
                END;

                BEGIN
                    DECLARE ss int default 0;
                    DECLARE uid int;
                    DECLARE c int;
                    DECLARE cur2 CURSOR FOR 
                    SELECT 
                        user_id,
                        IFNULL(COUNT(id),0)  
                    FROM join_uia 
                    WHERE ui_week = week2 
                    AND interaction_type in (1,2,3) 
                    AND i_career_level = cl 
                    AND i_week = week1 
                    GROUP BY user_id;
                    DECLARE CONTINUE HANDLER FOR NOT FOUND SET ss = 1;
                    open cur2;
                    FETCH cur2 into uid, c;
                    WHILE ss <> 1 DO
                        UPDATE sample 
                        SET usj_cl_2_p = c  
                        WHERE i_career_level = cl 
                        AND serial = ser 
                        AND user_id = uid;
                        FETCH cur2 into uid, c;
                    END WHILE;
                    CLOSE cur2;
                END;

                BEGIN
                    DECLARE ss int default 0;
                    DECLARE uid int;
                    DECLARE c int;
                    DECLARE cur2 CURSOR FOR 
                    SELECT 
                        user_id,
                        IFNULL(COUNT(id),0)  
                    FROM join_uia 
                    WHERE ui_week = week2 
                    AND interaction_type in (1,2,3) 
                    AND i_career_level = cl 
                    AND i_week = week2 
                    GROUP BY user_id;
                    DECLARE CONTINUE HANDLER FOR NOT FOUND SET ss = 1;
                    open cur2;
                    FETCH cur2 into uid, c;
                    WHILE ss <> 1 DO
                        UPDATE sample 
                        SET usj_cl_3_p = c  
                        WHERE i_career_level = cl 
                        AND serial = ser 
                        AND user_id = uid;
                        FETCH cur2 INTO uid, c;
                    END WHILE;
                    CLOSE cur2;
                END;

                BEGIN
                    DECLARE ss int default 0;
                    DECLARE uid int;
                    DECLARE c int;
                    DECLARE cur2 CURSOR FOR 
                    SELECT 
                        user_id,
                        IFNULL(COUNT(id),0)  
                    FROM join_uia 
                    WHERE ui_week = week1 
                    AND interaction_type = 4 
                    AND i_career_level = cl 
                    AND i_week = week1 
                    GROUP BY user_id;
                    DECLARE CONTINUE HANDLER FOR NOT FOUND SET ss = 1;
                    open cur2;
                    FETCH cur2 into uid, c;
                    WHILE ss <> 1 DO
                        UPDATE sample 
                        SET usj_cl_1_n = c  
                        WHERE i_career_level = cl 
                        AND serial = ser 
                        AND user_id = uid;
                        FETCH cur2 INTO uid, c;
                    END WHILE;
                    CLOSE cur2;
                END;

                BEGIN
                    DECLARE ss int DEFAULT 0;
                    DECLARE uid int;
                    DECLARE c int;
                    DECLARE cur2 CURSOR FOR 
                    SELECT 
                        user_id,
                        IFNULL(COUNT(id),0)  
                    FROM join_uia 
                    WHERE ui_week = week2 
                    AND interaction_type = 4 
                    AND i_career_level = cl 
                    AND i_week = week1 
                    GROUP BY user_id;
                    DECLARE CONTINUE HANDLER FOR NOT FOUND SET ss = 1;
                    open cur2;
                    FETCH cur2 into uid, c;
                    WHILE ss <> 1 DO
                        UPDATE sample 
                        SET usj_cl_2_n = c  
                        WHERE i_career_level = cl 
                        AND serial = ser 
                        AND user_id = uid;
                        FETCH cur2 INTO uid, c;
                    END WHILE;
                    CLOSE cur2;
                END;

                BEGIN
                    DECLARE ss int default 0;
                    DECLARE uid int;
                    DECLARE c int;
                    DECLARE cur2 CURSOR FOR 
                    SELECT 
                        user_id,
                        IFNULL(COUNT(id),0)  
                    FROM join_uia WHERE ui_week = week2 
                    AND interaction_type = 4 
                    AND i_career_level = cl 
                    AND i_week = week2 
                    GROUP BY user_id;
                    DECLARE CONTINUE HANDLER FOR NOT FOUND SET ss = 1;
                    open cur2;
                    FETCH cur2 into uid, c;
                    WHILE ss <> 1 DO
                        UPDATE sample 
                        SET usj_cl_3_n = c  
                        WHERE i_career_level = cl 
                        AND serial = ser 
                        AND user_id = uid;
                        FETCH cur2 into uid, c;
                    END WHILE;
                    CLOSE cur2;
                END;

                SET i = i + 1;
            END WHILE;

        END IF;
        FETCH cur INTO cl;
    END WHILE;

END
//
DELIMITER ;

CALL `t4_cl`()
