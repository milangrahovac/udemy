uninstall:
	helm uninstall local-wp
	# kubectl delete svc local-wp-np
	kubectl delete secret local-wp-mariadb
	kubectl delete secret local-wp-wordpress
	kubectl delete secret custom-wp-credentials
	kubectl delete pvc data-local-wp-mariadb-0
	kubectl delete pvc local-wp-wordpress
	kubectl delete pv pvc-5d63ddf4-33f8-4e42-a096-1aca03996b18
	kubectl delete pv pvc-bfb60bcf-75f7-4e24-a6e8-629121bdae00

install: uninstall
	helm install local-wp bitnami/wordpress --version=23.1.20
	kubectl expose deploy local-wp-wordpress --type=NodePort --name=local-wp
	minikube service local-wp  