# A simple CI/CD
This repository serves an example on how to have a CI/CD to deploy your services to a k8s cluster.
Github Action will do the following upon PR opening:
- Set up KinD cluster
- Set up Traefik for the ingress controller
- Deploy two sample echo services (foo and bar) and route: 
  - foo.localhost to foo service
  - bar.localhost to bar service
- Port-forward traefik to port 8080 and run load test using locust to foo and bar service
  - Github runner doesn't allow using host port 80 and map it to the container, so traefik is port-forwarded to port 8080
  - Load test is run to both foo and bar services with different header
  - Load test is run with this instruction:
    - Run for 30s
    - Ramped up to 100 users
    - With rate of 10 RPS
    - Each request will 
- Post the load test result as a comment in the PR

# Time
- 26th May 13.20 - 14:56:
  - Github Action for the CI created with this scope:
    - Setup KinD cluster
    - Deployed traefik as ingress controller
    - Deployed foo and bar services
    - Verify the IngressRoute (foo.localhost and bar.localhost)
    - PRs:
      - https://github.com/akbargumbira/ci_cd/pull/1 
      - https://github.com/akbargumbira/ci_cd/pull/2
- 26th May 15:16 - 