docker run \
    -p 8000:80 \
    -e AZURE_ACCOUNT_NAME="todaysfriend" \
    -e AZURE_ACCOUNT_KEY="kCaDvxw6wPgH9QmMtuZKerP+af2zok41DY/YyNV/Ar/ygbQjoymO1UWU0LJKlToWsyzDh5BWDZo2/hQkanohhg==" \
    -e DB_HOST="todaysfriend.postgres.database.azure.com" \
    -e DB_NAME="postgres" \
    -e DB_USER="jyg0172@todaysfriend" \
    -e DB_PASSWORD="aa72853572!!" \
    --rm -it \
    todaysfriend
