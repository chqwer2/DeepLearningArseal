

# if
if TEST-COMMAND
then
  STATEMENTS
fi


#如果文件夹不存在，创建文件夹
if [ ! -d "/myfolder" ]; then
  mkdir /myfolder
fi


folder="/var/www/"
file="/var/www/log"

# -d 参数判断 $folder 是否存在
if [ ! -d "$folder"]; then
  mkdir "$folder"
fi


# -f 参数判断 $file 是否存在
if [ ! -f "$file" ]; then
  touch "$file"
fi
