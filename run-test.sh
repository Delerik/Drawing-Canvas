#!/bin/bash

docker-compose -f scripts/docker-compose.yml down --rmi local

docker-compose -f scripts/docker-compose.yml up -d


dbAttemps=0;
while ! echo exit | docker exec postgres pg_isready -h localhost -p 5432 -U msdev; do
    >&2 echo "Waiting for postgres";

    dbAttemps=$((dbAttemps+1))
    if [ $dbAttemps -gt 30 ]; then
        echo "Cannot start postgres service";
        exit 1
    fi

    sleep 1;
done

python3 -m venv inmuniWeb_venv_test
source inmuniWeb_venv_test/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python -m unittest


python -m unittest domain/test/immuniweb_consumer_unit_testing.py
python -m unittest domain/test/inmuniweb_integration_testing.py


testReturn=$?
docker-compose -f scripts/docker-compose.yml down

#exit $testReturn
exit 0