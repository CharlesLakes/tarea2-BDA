docker:
	docker-compose up -d
replica:
	sh init-replica-set.sh
migrate:
	python3 migrate_data.py

