-- 코드를 입력하세요
SELECT concat('/home/grep/src/',USED_GOODS_FILE.BOARD_ID,'/',file_ID,file_name,file_ext) as FILE_PATH
FROM USED_GOODS_BOARD
join USED_GOODS_FILE  on USED_GOODS_BOARD.BOARD_ID = USED_GOODS_FILE.BOARD_ID
WHERE VIEWS = (SELECT MAX(VIEWS) FROM USED_GOODS_BOARD)
order by file_id desc
