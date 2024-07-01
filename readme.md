### Установка:

```bash
git clone https://github.com/ipodprugin/auchan-test-task.git && cd auchan-test-task
cp example.env .env
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Запуск:

```bash
python3 main.py
```

---

Python скрипт записывает в результирующий файл "развёрнутые" диапазоны.  
Если это не требуется, можно решить задачу таким небольшим bash скриптом:

```bash
#!/bin/bash

start_time=$(date +%s.%N)

for folder in $(find . -type d -name "TEST_Folder_*"); do
  for file in $(find "$folder" -type f -name "TEST_*"); do
    outfile=$(echo "$file" | sed 's/TEST_/TEST_AUCHAN_success_/g' | sed 's/\.[^.]*$/.txt/')
    outfile=$(echo "$outfile" | sed 's/.*\///')
    mkdir -p "Result"
    tr -d '\"' < "$file" | tr ',' '\n' | sort -n > "Result/$outfile"
  done
done

execution_time=$(echo "$(date +%s.%N) - $start_time" | bc)
echo "Время выполнения: $execution_time секунд"
```
