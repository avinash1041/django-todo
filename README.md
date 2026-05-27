
# ============================================================
#   COMPLETE DEVOPS & CLOUD INTERVIEW PREPARATION GUIDE
#   Beginner → Senior Level | All Topics Covered
#   For: Senior Software Engineer Interviews
# ============================================================

---

# ════════════════════════════════════════════
# PART 1 — GIT & GITHUB
# ════════════════════════════════════════════

## 1. What is Git?

**Simple definition:**
Git is like a "save button" for your code — but 100x smarter.
It remembers EVERY change you made, WHEN you made it, and WHO made it.

**Real-world example:**
You write a story (code). You save version 1, version 2, version 3.
Later you realize version 2 was better — Git lets you go back!

**Why used:**
- Track every code change
- Work with teams without overwriting each other
- Go back to any previous version
- See who changed what and why

---

## 2. What is GitHub?

**Simple definition:**
GitHub = Git + Internet storage.
Git is the tool. GitHub is the website that stores your code online.

Like Google Drive, but specifically for code with Git features.

**Other similar tools:** GitLab, Bitbucket

---

## 3. Core Git Concepts

### Repository (Repo)
A folder that Git is tracking. Your project folder.

```bash
git init         # make a folder into a git repo
git clone URL    # copy someone else's repo to your computer
```

### Commit
A "snapshot" of your code at a point in time. Like saving a game.

```bash
git add .           # stage all changes
git commit -m "message"   # save snapshot with message
```

### Push & Pull
```bash
git push    # upload your commits to GitHub
git pull    # download latest commits from GitHub
```

### Branch
A parallel version of your code. Like working on a copy.

```
main branch  → stable, production code
feature branch → your new feature, won't break main
```

```bash
git branch feature-login    # create branch
git checkout feature-login  # switch to branch
git checkout -b feature-login  # create + switch
```

### Merge
Combine two branches together.

```bash
git checkout main
git merge feature-login    # bring feature into main
```

### Rebase
Re-apply your commits on top of another branch.
Like picking up your work and moving it to a cleaner starting point.

```bash
git rebase main    # rebase current branch on main
```

**Merge vs Rebase:**
- Merge → keeps full history, creates merge commit
- Rebase → cleaner, linear history, rewrites commits

### Cherry-pick
Take ONE specific commit from another branch.

```bash
git cherry-pick abc1234    # copy just that one commit
```

### Stash
Temporarily save your work without committing.

```bash
git stash         # save changes temporarily
git stash pop     # bring them back
```

### Git Ignore (.gitignore)
Tell Git which files to NEVER track.

```
node_modules/
.env
*.log
```

### HEAD
HEAD = where you are right now in Git history.
Like a bookmark — it points to your current commit.

**Detached HEAD:**
When HEAD points to a commit instead of a branch.
Usually happens when you checkout an old commit directly.

```bash
git checkout abc1234   # detached HEAD
git checkout main      # back to normal
```

### Tags
A permanent label for a specific commit (e.g., v1.0.0 release).

```bash
git tag v1.0.0           # create tag
git push origin v1.0.0  # push tag to GitHub
```

### Git Hooks
Scripts that run automatically on Git events (pre-commit, post-push, etc.)
Used for: run tests before commit, lint code, send notifications.

---

## 4. Git Branching Strategies

### GitFlow (most common in companies)
```
main        → production-ready code
develop     → integration branch
feature/*   → new features
release/*   → preparing for release
hotfix/*    → emergency production fixes
```

### Trunk-Based Development
Only ONE main branch. Small, frequent commits.
Feature flags used to hide incomplete features.

### Feature Branch Strategy
Each feature = its own branch. Merge via Pull Request.

---

## 5. Pull Request (PR) & Code Review

**Pull Request = asking to merge your branch into main.**

Flow:
1. Developer creates feature branch
2. Writes code, pushes to GitHub
3. Opens Pull Request
4. Team reviews code (Code Review)
5. Approved → merged to main

**Why code review?**
- Catch bugs before production
- Share knowledge in team
- Maintain code quality standards

---

## 6. Merge Conflicts

Happens when two people edited the SAME line of code.

```
<<<<<<< HEAD (your version)
name = "Alice"
=======
name = "Bob"
>>>>>>> feature-branch (other version)
```

Fix: decide which version to keep, delete conflict markers, commit.

---

## 7. Git Workflow (Real Company Flow)

```
GitHub Repo (main)
       |
   git clone
       |
  Developer's laptop
       |
  git checkout -b feature/my-feature
       |
  Write code + git commit
       |
  git push origin feature/my-feature
       |
  Open Pull Request on GitHub
       |
  Code Review by team
       |
  Merge to main
       |
  CI/CD runs → Deploy to production
```

---

## 8. Git + CI/CD Integration

When code is pushed or PR is merged:
- GitHub Actions / Jenkins automatically:
  - Run tests
  - Build Docker image
  - Deploy to server

---

## 9. Important Git Interview Questions & Answers

**Q: What is the difference between git pull and git fetch?**
A: git fetch downloads changes but doesn't apply them.
   git pull = git fetch + git merge (downloads AND applies).

**Q: What is git rebase and when to use it?**
A: Rebase moves your commits to start from the latest main branch.
   Use for: keeping clean, linear history. Don't use on shared branches.

**Q: What is a detached HEAD?**
A: HEAD points to a commit, not a branch. Commits made here are "lost"
   unless you create a branch.

**Q: What is git cherry-pick?**
A: Copy a specific commit from one branch to another.
   Use case: hotfix on main, apply same fix to develop.

**Q: Explain GitFlow.**
A: main=production, develop=integration, feature branches for new work,
   release branch for preparing release, hotfix for emergency fixes.

**Q: How do you handle merge conflicts?**
A: Manually edit the conflicting file, choose correct code,
   delete conflict markers, git add, git commit.

**Q: What is the difference between merge and rebase?**
A: Merge creates a merge commit, keeps full history.
   Rebase rewrites history to be linear (cleaner but more risky).

---

## 10. Common Git Mistakes
- Committing to main directly (should use feature branches)
- Committing .env files with secrets (use .gitignore!)
- Force pushing to shared branches (git push --force destroys history)
- Large commits (commit small, often)
- Bad commit messages ("fix" vs "Fix login button null pointer error")

## 11. Git Best Practices
- Small, frequent commits
- Meaningful commit messages
- Always work on a branch
- Never commit secrets or passwords
- Review your own code before PR
- Keep branches short-lived (merge quickly)
- Use .gitignore properly

## 12. Memory Trick
```
Git = Camera (takes snapshots of code)
GitHub = Photo Album stored online
Branch = Parallel universe of your code
Merge = Combine two universes
Commit = One snapshot/photo
Push = Upload photos to album
Pull = Download latest photos
```

---

# ════════════════════════════════════════════
# PART 2 — DOCKER
# ════════════════════════════════════════════

## 1. What is Docker?

**Simple definition:**
Docker is a tool that packages your app and EVERYTHING it needs
(code, libraries, settings) into a neat box called a **Container**.

**Real-world analogy:**
Imagine you make a burger. You pack the burger, fries, sauce, everything
in one box. You can give that box to ANYONE and they get the exact
same burger — no matter what kitchen they use.

Docker does the same for software.

---

## 2. Why Docker?

**The Problem before Docker:**
"It works on my computer but not yours!"
- Different OS versions
- Different library versions
- Different configurations

**Docker solution:**
Everything needed is INSIDE the container.
Same container runs anywhere: laptop, server, cloud.

---

## 3. Virtual Machine (VM) vs Docker

```
VIRTUAL MACHINE:
[App A] [App B] [App C]
[Guest OS] [Guest OS] [Guest OS]
[      Hypervisor       ]
[         Host OS        ]
[         Hardware        ]

DOCKER:
[App A] [App B] [App C]
[ Docker Engine (daemon) ]
[         Host OS        ]
[         Hardware        ]
```

| Feature       | VM                    | Docker Container       |
|--------------|----------------------|------------------------|
| Size          | GBs (includes full OS) | MBs (shares host OS)  |
| Startup       | Minutes               | Seconds                |
| Isolation     | Strong (own OS)       | Process-level          |
| Performance   | Slower                | Near-native            |
| Use case      | Full OS needed        | App packaging          |

**Key insight:** Containers share the HOST OS kernel. VMs have their own.

---

## 4. Docker Key Concepts

### Image
A blueprint/recipe for a container.
Like a cookie cutter — from ONE image you can make MANY containers.

```bash
docker images              # list images
docker pull nginx          # download nginx image
docker build -t myapp .    # build image from Dockerfile
```

### Container
A running instance of an image.
Image = recipe. Container = the actual dish.

```bash
docker run nginx           # create + start container
docker ps                  # list running containers
docker stop container_id   # stop container
docker rm container_id     # delete container
```

### Dockerfile
A text file with instructions to build your image.

```dockerfile
FROM node:18
WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
EXPOSE 3000
CMD ["node", "server.js"]
```

Each line = one layer. Layers are CACHED (makes rebuilds fast).

### Docker Compose
Run MULTIPLE containers together as a group.

```yaml
version: '3'
services:
  web:
    build: .
    ports:
      - "3000:3000"
  db:
    image: postgres
    environment:
      POSTGRES_PASSWORD: secret
```

```bash
docker-compose up    # start all services
docker-compose down  # stop all services
```

### Volumes
Persistent storage for containers.
Containers are temporary — when deleted, data is gone.
Volumes save data even if container is deleted.

```bash
docker run -v /host/path:/container/path nginx
```

### Networks
How containers talk to each other.

```bash
docker network create mynet
docker run --network mynet myapp
```

### Port Mapping
Map container port to host port.

```bash
docker run -p 8080:3000 myapp
# host port 8080 → container port 3000
```

### Environment Variables
Pass configuration to containers.

```bash
docker run -e DB_URL=postgres://... myapp
```

---

## 5. Multi-Stage Build

Build smaller production images by using multiple FROM statements.

```dockerfile
# Stage 1: Build
FROM node:18 AS builder
WORKDIR /app
COPY . .
RUN npm install && npm run build

# Stage 2: Production (only copy built files)
FROM node:18-alpine
WORKDIR /app
COPY --from=builder /app/dist .
CMD ["node", "index.js"]
```

Result: Final image is MUCH smaller (no build tools, no dev dependencies).

---

## 6. Docker Architecture

```
Docker CLI (you type commands)
         |
Docker Daemon (dockerd) — the engine running on your machine
         |
    Container Runtime
    |         |
Container1  Container2
```

**Docker Registry:**
A storage place for Docker images.
- Docker Hub = public registry (like GitHub for images)
- ECR = AWS private registry
- GCR = Google Container Registry

```bash
docker push myrepo/myapp:v1   # upload image to registry
docker pull myrepo/myapp:v1   # download image from registry
```

---

## 7. Container Lifecycle

```
Created → Running → Paused → Stopped → Deleted
```

```bash
docker create    # create (not started)
docker start     # start created container
docker run       # create + start together
docker pause     # freeze container
docker stop      # graceful stop (SIGTERM)
docker kill      # force stop (SIGKILL)
docker rm        # delete stopped container
```

---

## 8. Docker Security Best Practices

- Never run as root inside container (add USER directive)
- Use minimal base images (alpine)
- Scan images for vulnerabilities (docker scout, trivy)
- Never store secrets in Dockerfile or image
- Use read-only filesystem when possible
- Keep images up to date

---

## 9. Docker Optimization

- Use .dockerignore (like .gitignore for Docker)
- Order Dockerfile layers: least-changed first, most-changed last
- Use multi-stage builds for small production images
- Use Alpine base images (5MB vs 300MB Ubuntu)
- Cache npm/pip install layers separately

---

## 10. Docker Swarm (basics)

Docker's built-in clustering tool. Manages multiple Docker hosts.
Simpler than Kubernetes but less powerful.

**When to use:** Small teams, simple deployments.
**When NOT to use:** Complex production scale (use Kubernetes instead).

---

## 11. Important Docker Interview Questions & Answers

**Q: What is the difference between an Image and a Container?**
A: Image = blueprint (static). Container = running instance (dynamic).
   From one image you can run many containers.

**Q: What is a Dockerfile?**
A: A text file with step-by-step instructions to build a Docker image.
   Each instruction = one layer.

**Q: What are Docker volumes and why needed?**
A: Containers are stateless — data is lost when deleted.
   Volumes provide persistent storage that outlives the container.

**Q: What is Docker Compose?**
A: A tool to define and run multi-container apps using a YAML file.
   Example: run your app + database + redis together.

**Q: What is multi-stage build?**
A: Using multiple FROM statements in a Dockerfile.
   Build in one stage, copy only needed files to final stage.
   Result: much smaller production images.

**Q: How does Docker networking work?**
A: By default, containers are isolated. You can create networks
   so containers can communicate. Bridge, host, overlay networks.

**Q: VM vs Docker?**
A: VMs include full OS (GBs, slow). Docker containers share host OS
   (MBs, fast). Docker is lighter, faster, uses less resources.

**Q: How do you pass environment variables to a container?**
A: Use -e flag: `docker run -e DB_HOST=localhost myapp`
   Or use --env-file for multiple variables.

---

## 12. Common Docker Mistakes
- Storing secrets in Dockerfile (use env vars or secrets management)
- Not using .dockerignore (copies node_modules into image)
- Running containers as root user
- Not using multi-stage builds (bloated images)
- Putting frequently changing files early in Dockerfile (breaks cache)

## 13. Memory Trick
```
Docker = Shipping Container for Software
Dockerfile = Recipe to build the container
Image = Pre-made packed container (not running)
Container = Running container (opened and working)
Volume = External hard drive for the container
Compose = Manager of multiple containers
Registry = Warehouse to store containers
```

---

# ════════════════════════════════════════════
# PART 3 — MICROSERVICES
# ════════════════════════════════════════════

## 1. What are Microservices?

**Simple definition:**
Break one BIG application into MANY SMALL independent services.
Each service does ONE thing only and can be deployed separately.

**Real-world analogy:**
A restaurant with specialized stations:
- One chef ONLY makes pizza
- One chef ONLY makes salad
- One chef ONLY makes dessert

Each works independently. If the salad chef is sick, pizza still works!

---

## 2. Monolith vs Microservices

```
MONOLITH — Everything in ONE big app
[User Auth + Products + Orders + Payments + Notifications]
     All in ONE codebase, ONE database, ONE deployment

MICROSERVICES — Many small apps
[User Service] [Product Service] [Order Service]
[Payment Service] [Notification Service]
Each has OWN codebase, OWN database, OWN deployment
```

| Feature          | Monolith             | Microservices          |
|-----------------|---------------------|------------------------|
| Codebase         | Single              | Multiple               |
| Deployment       | All at once         | Independent            |
| Scaling          | Scale everything    | Scale only needed part |
| Failure          | One failure = all down | Isolated failure    |
| Team size        | Small teams OK      | Better for large teams |
| Complexity       | Simple initially    | Complex from start     |
| Database         | Shared              | One per service        |
| Development      | Fast initially      | Slow initially         |

---

## 3. Why Microservices?

✅ **Scale independently:** High traffic on payments? Scale only payment service.
✅ **Deploy independently:** Update one service without deploying everything.
✅ **Fault isolation:** One service fails, others continue working.
✅ **Technology flexibility:** Each team can use different languages/DB.
✅ **Smaller codebases:** Easier to understand and maintain.

❌ **Disadvantages:**
- Complex infrastructure
- Network latency between services
- Distributed system problems (data consistency)
- More operational overhead
- Harder debugging

---

## 4. Service Communication

### Synchronous (direct, waits for response)
**REST API:** HTTP-based, most common

```
Service A → HTTP POST → Service B → Response → Service A
```

**gRPC:** Faster than REST, uses Protocol Buffers, ideal for internal services

### Asynchronous (sends and forgets, via message queue)
**Kafka / RabbitMQ:**

```
Order Service → publishes event → Kafka → Payment Service (consumes)
                                         → Email Service (consumes)
```

**When to use which:**
- Sync: Need immediate response (check stock, get user info)
- Async: Don't need immediate response (send email, process payment)

---

## 5. API Gateway

The SINGLE entry point for all client requests.
Clients talk to one place; gateway routes to correct service.

```
Client App
    |
  [API Gateway]  ← single entry point
    |      |      |
[User]  [Orders]  [Products]  ← microservices
```

**API Gateway does:**
- Routing
- Authentication
- Rate limiting
- Load balancing
- SSL termination
- Logging

---

## 6. Service Discovery

How do services find each other?
Services can go up/down, have dynamic IPs. Need a registry.

```
Service A wants to talk to Service B
→ Asks Service Registry: "Where is Service B?"
→ Registry returns: "10.0.0.5:8080"
→ Service A calls that address
```

Tools: Consul, Eureka, Kubernetes DNS (built-in)

---

## 7. Database Per Service Pattern

Each microservice has its OWN database. No sharing!

```
[User Service] → [Users DB]
[Order Service] → [Orders DB]
[Product Service] → [Products DB]
```

**Why?** Loose coupling. Each service can choose best DB type for its needs.
**Problem?** Data consistency across services is hard.

---

## 8. Event-Driven Architecture

Services communicate via EVENTS (messages).
Services don't call each other directly — they publish events.

```
[Order Service] → "OrderPlaced" event → [Message Bus (Kafka)]
                                               |
                              [Payment Service] consumes
                              [Email Service] consumes
                              [Inventory Service] consumes
```

**Benefits:** Loose coupling, scales well, services don't block each other.

---

## 9. Fault Tolerance Patterns

### Circuit Breaker
Like an electrical circuit breaker.
If Service B keeps failing, stop calling it. Return cached/default response.

```
Service A → Service B [FAILING]
After 5 failures → Circuit OPEN → Don't call B for 30 seconds
After 30 seconds → Try again → If success → Circuit CLOSED
```

Tools: Netflix Hystrix, Resilience4j

### Retry Mechanism
Automatically retry failed requests with exponential backoff.

```
Try 1 → fails → wait 1s
Try 2 → fails → wait 2s
Try 3 → fails → wait 4s → give up
```

### Timeout
Don't wait forever. Set a maximum wait time.

---

## 10. Distributed Tracing

When a request goes through 10 services, how do you trace it?
Assign ONE trace ID to the request, pass it through all services.

Tools: Jaeger, Zipkin, AWS X-Ray

```
Request comes in → Trace ID: abc123
→ Service A [abc123] → Service B [abc123] → Service C [abc123]
Now you can see the FULL journey with timing!
```

---

## 11. Netflix/Uber Real Architecture (Basics)

**Netflix:**
- 700+ microservices
- API Gateway handles all requests
- Services communicate via REST and Kafka
- Each service auto-scales on AWS
- Chaos Engineering: intentionally kills services to test resilience

**Uber:**
- Separate services: driver, rider, pricing, maps, payments
- Event-driven for ride matching
- gRPC for internal communication
- Kafka for high-volume event streaming

---

## 12. Important Microservices Interview Questions

**Q: What is a microservice?**
A: Small, independently deployable service that does ONE thing.
   Has its own codebase, database, and deployment pipeline.

**Q: When NOT to use microservices?**
A: Small teams, early-stage startups, simple apps.
   Monolith first, split into microservices when truly needed.

**Q: What is an API Gateway?**
A: Single entry point for all client requests.
   Handles routing, auth, rate limiting.

**Q: How do microservices communicate?**
A: Sync: REST or gRPC (waits for response).
   Async: Message queues like Kafka (fire and forget).

**Q: What is Circuit Breaker pattern?**
A: Stop calling a failing service after repeated failures.
   Give it time to recover. Prevents cascading failures.

**Q: How to handle distributed transactions?**
A: SAGA pattern: series of local transactions with compensating actions if one fails.

**Q: What is Service Discovery?**
A: A registry where services register themselves.
   Other services ask registry to find them.

---

## 13. Common Mistakes
- Creating too many microservices too early (nanoservice hell)
- Sharing databases between services
- Synchronous calls everywhere (use async where possible)
- Not implementing circuit breakers
- No distributed tracing (impossible to debug)

## 14. Memory Trick
```
Microservices = Restaurant Kitchen
Each service = One chef station (does only one thing)
API Gateway = Head waiter (routes orders to right chef)
Kafka = Order tickets passed between stations
Circuit Breaker = "Station is overwhelmed, pause orders"
Service Discovery = Staff directory ("Where is the chef?")
```

---

# ════════════════════════════════════════════
# PART 4 — AWS ECS
# ════════════════════════════════════════════

## 1. What is AWS ECS?

**Simple definition:**
ECS (Elastic Container Service) = AWS's service to run Docker containers
at scale in the cloud.

**Real-world analogy:**
You have many workers (Docker containers).
ECS is the manager who assigns them jobs, restarts them if they fail,
adds more workers when busy.

---

## 2. Key ECS Concepts

### Cluster
A group of servers/resources where containers run.
Like a building — containers run inside it.

### Task Definition
A blueprint (like Dockerfile but for ECS).
Describes: which Docker image, CPU, memory, ports, env vars.

### Task
A running instance of a Task Definition.
Like running `docker run` but managed by ECS.

### Service
Ensures a specified number of Tasks are ALWAYS running.
If a task crashes → service automatically starts a new one!

```
ECS Service → "I need 3 tasks running at all times"
Task 1 crashes → Service immediately starts Task 4
```

---

## 3. Launch Types

### Fargate (Serverless)
AWS manages the servers for you.
You just define CPU + memory. AWS handles the rest.
✅ No server management
✅ Pay per task
❌ Less control, slightly more expensive

### EC2 Launch Type
You manage the EC2 servers that containers run on.
✅ More control, cheaper at scale
❌ You manage servers (patching, scaling, etc.)

**Rule of thumb:** Start with Fargate. Switch to EC2 when scale justifies it.

---

## 4. ECR (Elastic Container Registry)

AWS's private Docker registry.
Like Docker Hub, but private and inside AWS.

```bash
# Authenticate
aws ecr get-login-password | docker login --username AWS --password-stdin <ECR_URL>

# Tag image
docker tag myapp:latest <ECR_URL>/myapp:latest

# Push
docker push <ECR_URL>/myapp:latest
```

---

## 5. ECS Deployment Flow (Step by Step)

```
1. Developer writes code
2. Docker image built (docker build)
3. Image pushed to ECR
4. Update Task Definition (new image URI)
5. Update ECS Service (point to new task definition)
6. ECS performs rolling deployment:
   - Starts new tasks with new version
   - Waits for health checks to pass
   - Stops old tasks
7. Load Balancer routes traffic to new tasks
```

---

## 6. ECS Architecture

```
Internet
    |
[Application Load Balancer]
    |
[ECS Service]
    |
[Task 1] [Task 2] [Task 3]  ← running containers
    |
[ECS Cluster]  ← Fargate (AWS manages servers) or EC2
```

---

## 7. Auto Scaling

ECS Service Auto Scaling adds/removes tasks based on load.

```
CPU usage > 70%? → Add 2 more tasks
CPU usage < 30%? → Remove 1 task
```

Types:
- Target Tracking (maintain CPU at 60%)
- Step Scaling (add N tasks when CPU > X%)

---

## 8. ECS Networking

### awsvpc Mode (recommended for Fargate)
Each task gets its OWN private IP address.
Can attach security groups directly to task.

### bridge Mode (EC2 only)
Tasks share the EC2 host's network.

---

## 9. IAM Roles in ECS

**Task Execution Role:** ECS agent permissions (pull images, write logs).
**Task Role:** YOUR app's permissions (read S3, write DynamoDB, etc.).

---

## 10. ECS Monitoring

- **CloudWatch Logs:** All container logs go here
- **CloudWatch Metrics:** CPU, memory, task count
- **ECS Service Events:** Why tasks stopped/started

---

## 11. Important ECS Interview Questions

**Q: What is the difference between a Task and a Service?**
A: Task is a running container instance. Service manages tasks —
   ensures N tasks always running, replaces failed tasks, handles deployments.

**Q: Fargate vs EC2 launch type?**
A: Fargate = serverless, AWS manages servers, pay per task.
   EC2 = you manage servers, more control, better for high scale/cost.

**Q: How does ECS deployment work?**
A: New image pushed to ECR → Update task definition → Update service →
   ECS does rolling update (new tasks up, health check passes, old tasks down).

**Q: What is a Task Definition?**
A: JSON blueprint describing container: image, CPU, memory, ports,
   environment variables, logging config.

**Q: How does ECS scaling work?**
A: Auto Scaling policy watches CPU/memory metrics.
   Adds tasks when load increases, removes when load decreases.

**Q: How do containers in ECS access AWS services (S3, DynamoDB)?**
A: Via IAM Task Role assigned to the task definition.
   No credentials in code — uses IAM role.

---

## 12. ECS vs Kubernetes (Quick)

| Feature       | ECS                   | Kubernetes             |
|--------------|----------------------|------------------------|
| Complexity    | Simple               | Complex                |
| AWS Integration | Native/deep        | Needs EKS setup        |
| Flexibility   | AWS only             | Any cloud              |
| Learning curve | Low                 | High                   |
| Cost          | Low overhead         | Higher (EKS control plane) |
| Use case      | AWS-first teams      | Multi-cloud, complex   |

---

# ════════════════════════════════════════════
# PART 5 — TERRAFORM
# ════════════════════════════════════════════

## 1. What is Terraform?

**Simple definition:**
Terraform lets you describe your ENTIRE infrastructure (servers, databases,
networks) as CODE in files, then automatically creates it all.

**Real-world analogy:**
Instead of manually building a LEGO house brick by brick,
you write a blueprint (code), and Terraform builds the house for you.
Want to build the same house in 5 cities? Run the same code 5 times!

---

## 2. Infrastructure as Code (IaC)

Before IaC: Click around in AWS console manually. Error-prone. Not repeatable.
With IaC: Write code → run it → infrastructure created automatically.

**Benefits:**
- Version control your infrastructure
- Reproduce environments (dev/staging/prod) identically
- Review infrastructure changes like code changes
- Disaster recovery: recreate entire infrastructure from code

---

## 3. Why Terraform?

✅ Works with 300+ providers (AWS, Azure, GCP, Kubernetes, etc.)
✅ Declarative: describe WHAT you want, not HOW to create it
✅ State management: knows what already exists
✅ Plan before apply: preview changes before making them
✅ Community modules: reuse others' work

---

## 4. Core Terraform Concepts

### Providers
Tell Terraform which cloud/service to use.

```hcl
terraform {
  required_providers {
    aws = { source = "hashicorp/aws" version = "~> 5.0" }
  }
}
provider "aws" { region = "us-east-1" }
```

### Resources
The actual infrastructure items to create.

```hcl
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"
}
```

### Variables
Make your code reusable by parameterizing values.

```hcl
variable "environment" { default = "dev" }
resource "aws_s3_bucket" "data" {
  bucket = "myapp-${var.environment}-data"
}
```

### Outputs
Print values after apply (like return values).

```hcl
output "server_ip" {
  value = aws_instance.web.public_ip
}
```

### State File
Terraform tracks what it created in a STATE FILE (terraform.tfstate).
It compares current state with desired state to know what to create/modify/delete.

⚠️ NEVER manually edit state file.
Store remotely (S3 + DynamoDB for AWS) so team can share.

---

## 5. Core Terraform Commands

```bash
terraform init      # download providers/plugins
terraform plan      # preview: what will be created/changed/destroyed?
terraform apply     # actually create/change infrastructure
terraform destroy   # delete everything Terraform created
terraform fmt       # format code
terraform validate  # check for errors
terraform output    # show output values
terraform state list # show what's in state
```

---

## 6. Modules

Reusable pieces of Terraform code.

```hcl
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.0.0"
  name    = "my-vpc"
  cidr    = "10.0.0.0/16"
}
```

Like functions in programming — write once, use many times.

---

## 7. Remote State

Store state file in S3 so team can collaborate safely.

```hcl
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-lock"  # prevents simultaneous applies
  }
}
```

---

## 8. Workspaces

Multiple state files in one config. Used for dev/staging/prod.

```bash
terraform workspace new staging
terraform workspace select production
terraform workspace list
```

---

## 9. Terraform Architecture

```
Developer writes .tf files
→ terraform init (downloads providers)
→ terraform plan (creates execution plan)
→ Terraform reads state file (what exists?)
→ Terraform computes DIFF (what needs to change?)
→ terraform apply (makes API calls to cloud)
→ State file updated
```

---

## 10. Important Terraform Interview Questions

**Q: What is Terraform State?**
A: A file (terraform.tfstate) that tracks what infrastructure Terraform created.
   Terraform compares desired state (code) vs current state (state file)
   to determine what changes to make.

**Q: What happens if state file is deleted?**
A: Terraform thinks nothing exists. Running apply will try to CREATE everything again.
   Use remote state (S3) to prevent loss. Can re-import resources.

**Q: What is terraform plan?**
A: Shows a preview of what WILL happen if you run apply.
   Shows creates (+), changes (~), destroys (-). Always run before apply!

**Q: What is the difference between Terraform and CloudFormation?**
A: Terraform: multi-cloud, open source, HCL language.
   CloudFormation: AWS only, managed by AWS, YAML/JSON.

**Q: How do you manage secrets in Terraform?**
A: Never hardcode. Use: AWS Secrets Manager, environment variables,
   HashiCorp Vault, SSM Parameter Store.

**Q: What is a Terraform module?**
A: Reusable Terraform code package. Like a function.
   Use to avoid repeating yourself.

**Q: What is terraform taint?**
A: Marks a resource to be destroyed and recreated on next apply.
   (Replaced by -replace in newer versions)

---

## 11. Terraform Best Practices
- Always use remote state (S3 + DynamoDB lock)
- Use modules for reusable infrastructure
- Use workspaces for environment separation
- Never commit tfstate files to Git
- Never hardcode secrets
- Use terraform plan in CI/CD before applying
- Tag all resources (owner, environment, project)
- Use versions for providers and modules

## 12. Memory Trick
```
Terraform = Builder with blueprints
.tf files = blueprints (what you want)
State file = inventory (what exists)
Plan = "Here's what I'll build" (preview)
Apply = Actually builds it
Destroy = Demolishes everything
Provider = Contractor who knows HOW to build for AWS/GCP/Azure
Module = Pre-made blueprint section (reuse it!)
```

---

# ════════════════════════════════════════════
# PART 6 — KUBERNETES
# ════════════════════════════════════════════

## 1. What is Kubernetes?

**Simple definition:**
Kubernetes (K8s) is like a very smart manager for your Docker containers.
It makes sure the right number of containers are running, restarts failed ones,
distributes traffic, and scales up/down automatically.

**Real-world analogy:**
You have 100 workers (containers). Kubernetes is the HR manager + scheduler:
- Makes sure the right workers are working
- Replaces sick workers automatically
- Hires more workers when work increases
- Gives workers the right tasks

---

## 2. Why Kubernetes?

Problem: You have 100 Docker containers across 50 servers. How do you:
- Make sure they keep running?
- Scale up during traffic spikes?
- Deploy new versions without downtime?
- Route traffic correctly?

Kubernetes solves ALL of this.

---

## 3. Docker vs Kubernetes

| Feature    | Docker               | Kubernetes                     |
|-----------|---------------------|-------------------------------|
| Purpose    | Package apps         | Manage apps at scale          |
| Scale      | Single server        | Cluster of servers            |
| Healing    | No                  | Yes (restarts failed containers)|
| Rolling updates | Manual         | Automatic                     |
| Use together? | Yes!             | Kubernetes RUNS Docker containers|

---

## 4. Kubernetes Architecture

```
CONTROL PLANE (Master Node)
┌─────────────────────────────────────────────┐
│ API Server   | Scheduler | Controller Manager│
│ etcd (DB)                                   │
└─────────────────────────────────────────────┘
         |
WORKER NODES
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│   Node 1    │  │   Node 2    │  │   Node 3    │
│ kubelet     │  │ kubelet     │  │ kubelet     │
│ [Pod][Pod]  │  │ [Pod][Pod]  │  │ [Pod][Pod]  │
└─────────────┘  └─────────────┘  └─────────────┘
```

**Control Plane components:**
- **API Server:** All communication goes through here (like receptionist)
- **Scheduler:** Decides which node to run new pods on
- **Controller Manager:** Watches and ensures desired state is maintained
- **etcd:** The database storing cluster state (critical!)

**Worker Node components:**
- **kubelet:** Agent on each node, follows instructions from control plane
- **kube-proxy:** Handles networking/routing on the node
- **Container Runtime:** Actually runs containers (Docker/containerd)

---

## 5. Core Kubernetes Objects

### Pod
The SMALLEST unit in Kubernetes.
Usually contains ONE container (sometimes 2-3 tightly coupled containers).

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
    - name: app
      image: nginx
      ports:
        - containerPort: 80
```

### Deployment
Manages a set of identical pods. Handles rolling updates.
YOU define desired state: "I want 3 nginx pods". K8s makes it happen.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx:1.21
```

### ReplicaSet
Ensures N copies of a pod are always running.
Deployment manages ReplicaSet. You usually don't create ReplicaSet directly.

### Service
A stable way to access pods. Pods have changing IPs; Services have stable IPs.

Types:
- **ClusterIP:** Internal access only (default)
- **NodePort:** Expose on each node's port
- **LoadBalancer:** Create a cloud load balancer

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: nginx
  ports:
    - port: 80
      targetPort: 80
  type: LoadBalancer
```

### Ingress
HTTP/HTTPS routing. Like an API Gateway at the K8s level.
Routes traffic to different services based on URL path.

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ingress
spec:
  rules:
    - host: myapp.com
      http:
        paths:
          - path: /api
            pathType: Prefix
            backend:
              service: { name: api-service, port: { number: 80 } }
          - path: /
            pathType: Prefix
            backend:
              service: { name: web-service, port: { number: 80 } }
```

### ConfigMap
Store non-sensitive configuration as key-value pairs.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  DATABASE_HOST: "postgres-service"
  APP_ENV: "production"
```

### Secret
Like ConfigMap but for sensitive data (passwords, tokens).
Values are base64 encoded (NOT encrypted by default!).

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
data:
  password: cGFzc3dvcmQ=  # base64 encoded
```

### Namespace
Logical separation of resources within a cluster.
Like folders. Use for: dev/staging/prod, different teams.

```bash
kubectl create namespace dev
kubectl get pods -n dev
```

---

## 6. Special Workload Types

### StatefulSet
Like Deployment, but for STATEFUL apps (databases).
Pods get stable names (pod-0, pod-1) and stable storage.
Used for: MySQL, PostgreSQL, MongoDB, Kafka.

### DaemonSet
Run ONE pod on EVERY node in the cluster.
Used for: log collectors, monitoring agents.

### Job
Run a pod until it completes successfully. Then it's done.
Used for: database migrations, batch jobs.

### CronJob
Run a Job on a schedule (like Linux cron).

```yaml
spec:
  schedule: "0 2 * * *"  # every day at 2 AM
```

---

## 7. Scaling

### Manual Scaling
```bash
kubectl scale deployment nginx --replicas=5
```

### HPA (Horizontal Pod Autoscaler)
Automatically add/remove pods based on CPU/memory.

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: nginx-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: nginx-deployment
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

---

## 8. Storage in Kubernetes

### Persistent Volume (PV)
A piece of storage in the cluster (like an external hard drive).
Created by admin or dynamically provisioned.

### Persistent Volume Claim (PVC)
A request for storage by a pod.
"I need 10GB of storage" → K8s finds/creates a PV.

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: data-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
```

---

## 9. Rolling Updates

Kubernetes updates pods gradually with ZERO downtime.

```
Old: [v1][v1][v1][v1][v1]
Step 1: [v1][v1][v1][v1][v2]
Step 2: [v1][v1][v1][v2][v2]
Step 3: [v1][v1][v2][v2][v2]
...
Done: [v2][v2][v2][v2][v2]
```

Always some pods running, so no downtime!

**Rollback:**
```bash
kubectl rollout undo deployment/nginx
```

---

## 10. Helm

Package manager for Kubernetes. Like apt/yum but for K8s apps.
Packages K8s resources into a "chart" that can be installed easily.

```bash
helm install my-release nginx/nginx-ingress
helm upgrade my-release nginx/nginx-ingress
helm rollback my-release 1
```

---

## 11. kubectl Commands

```bash
kubectl get pods              # list pods
kubectl get pods -o wide      # with node info
kubectl describe pod my-pod   # detailed info
kubectl logs my-pod           # container logs
kubectl exec -it my-pod -- bash  # shell into pod
kubectl apply -f deployment.yaml  # apply config
kubectl delete -f deployment.yaml # delete resources
kubectl get events             # cluster events
kubectl top pods               # CPU/memory usage
```

---

## 12. Kubernetes Security

- **RBAC:** Role-Based Access Control. Who can do what.
- **Network Policies:** Control which pods can talk to which.
- **Pod Security Context:** Run as non-root, read-only filesystem.
- **Secrets:** Use external secrets managers (AWS Secrets Manager + External Secrets).
- **Image scanning:** Scan images for vulnerabilities before deploying.

---

## 13. Important Kubernetes Interview Questions

**Q: What is a Pod?**
A: Smallest deployable unit. Usually one container.
   Has its own IP, storage, network namespace.

**Q: What is the difference between Deployment and StatefulSet?**
A: Deployment: stateless apps, pods are interchangeable.
   StatefulSet: stateful apps (DBs), pods have stable identity and storage.

**Q: What happens when a node fails?**
A: Controller Manager detects node failure.
   Pods on that node are rescheduled to other healthy nodes.
   This is self-healing!

**Q: What is the difference between Service types?**
A: ClusterIP: internal. NodePort: exposed on node port.
   LoadBalancer: creates cloud LB. Ingress: HTTP routing rules.

**Q: What is HPA?**
A: Horizontal Pod Autoscaler. Automatically scales pod count
   based on metrics (CPU, memory, custom).

**Q: How do you do zero-downtime deployment?**
A: Rolling update strategy in Deployment spec.
   K8s gradually replaces old pods with new ones.

**Q: What is etcd?**
A: Distributed key-value store used by K8s as its "brain"/database.
   Stores entire cluster state. Critical component — backup regularly!

**Q: What is a ConfigMap vs Secret?**
A: ConfigMap: non-sensitive config data.
   Secret: sensitive data (passwords, tokens). Base64 encoded.
   For real security, use Vault or AWS Secrets Manager.

**Q: How does Service Discovery work in K8s?**
A: Built-in DNS. Every Service gets a DNS name.
   `my-service.my-namespace.svc.cluster.local`
   Pods find each other by service name.

---

## 14. Memory Trick
```
Kubernetes = Airport Manager
Pod = Airplane (holds passengers/containers)
Node = Airport terminal
Deployment = Airline schedule (how many planes, which route)
Service = Boarding gate (stable way to reach pods)
Ingress = Airport entrance (routes to correct gate)
HPA = Add more flights when demand is high
ConfigMap = Flight information board
Secret = Locked safe (sensitive info)
Namespace = Different terminals (dev/prod separation)
```

---

# ════════════════════════════════════════════
# PART 7 — KAFKA
# ════════════════════════════════════════════

## 1. What is Kafka?

**Simple definition:**
Kafka is a super fast, distributed message bus that allows services to
communicate by PUBLISHING and CONSUMING events/messages.

**Real-world analogy:**
Think of Kafka as a news broadcast system:
- Journalists (Producers) write stories
- Stories go to a TV network (Kafka)
- Viewers (Consumers) watch the stories

Multiple viewers can watch the SAME story. The story is stored for days.
New viewers can watch old stories (replay).

---

## 2. Why Kafka?

| Problem                           | Kafka Solution                        |
|-----------------------------------|--------------------------------------|
| Service A needs to notify 10 services | Publish ONE event, all 10 consume |
| Process millions of events/second  | Kafka handles millions/sec           |
| Message gets lost if consumer down | Kafka stores messages for days       |
| Need to replay past events         | Kafka stores and can replay          |
| Multiple apps need same data       | Multiple consumer groups             |

---

## 3. Core Kafka Concepts

### Producer
Sends (publishes) messages to Kafka.

```
Order Service → [OrderPlaced event] → Kafka
```

### Consumer
Reads (consumes) messages from Kafka.

```
Kafka → [OrderPlaced event] → Payment Service
Kafka → [OrderPlaced event] → Email Service
```

### Broker
A Kafka server. A cluster has multiple brokers for reliability.

### Topic
A named stream/channel of messages.
Like a TV channel — producers write to it, consumers read from it.

```
Topics: user-events, order-events, payment-events
```

### Partition
Topics are split into partitions for parallelism and scale.

```
Topic: orders
  Partition 0: [msg1, msg4, msg7]
  Partition 1: [msg2, msg5, msg8]
  Partition 2: [msg3, msg6, msg9]
```

**Key insight:** Messages with same key always go to same partition.
This ensures ORDER for related messages.

### Offset
Position of a message in a partition. Like a page number.
Each message has a unique offset within its partition.

Consumers track their offset to know where they are.

### Consumer Group
Multiple consumers working together to consume a topic.
Each partition is consumed by ONLY ONE consumer in the group.

```
Topic: orders (3 partitions)
Consumer Group: payment-service

Consumer A → reads Partition 0
Consumer B → reads Partition 1
Consumer C → reads Partition 2

Add Consumer D? One consumer will be idle (more partitions than consumers)
Remove Consumer C? Consumer A or B takes over Partition 2
```

---

## 4. Kafka Architecture

```
Producers
   |
[Kafka Cluster]
  [Broker 1]  [Broker 2]  [Broker 3]
  Each broker has some topic partitions
  Partitions are REPLICATED across brokers
   |
Consumers (Consumer Groups)
```

### ZooKeeper / KRaft
- Old Kafka: ZooKeeper managed cluster metadata
- New Kafka: KRaft mode (Kafka itself manages metadata, no ZooKeeper needed)

---

## 5. Retention

Kafka stores messages for a configured time (default: 7 days).
Consumers can re-read old messages!

This is different from traditional queues (RabbitMQ) where messages are
deleted after consumption.

---

## 6. Replication

Each partition has REPLICAS across multiple brokers.

```
Partition 0 Leader: Broker 1
Partition 0 Replica: Broker 2, Broker 3
```

If Broker 1 fails → Broker 2 or 3 becomes new leader.
Data is NOT lost.

**Replication Factor:** How many copies of each partition.
Typical production: 3 (one leader + 2 replicas).

---

## 7. Message Flow (End to End)

```
1. Producer sends message to Topic "orders", key="user123"
2. Kafka determines partition (hash of key % numPartitions)
3. Message stored in partition with next available offset
4. Message replicated to replica brokers
5. Consumer Group polls for new messages
6. Consumer reads message, processes it
7. Consumer commits offset (says "I've processed up to here")
8. If consumer crashes before commit → re-reads same message
   (at-least-once delivery)
```

---

## 8. Kafka vs RabbitMQ

| Feature          | Kafka                          | RabbitMQ                    |
|-----------------|--------------------------------|----------------------------|
| Type             | Event streaming platform       | Message queue               |
| Message storage  | Stores for days/weeks          | Deletes after consumption   |
| Throughput       | Millions/sec                   | Thousands/sec               |
| Replay           | Yes (read old messages)        | No                          |
| Consumer groups  | Multiple independent groups    | Competing consumers         |
| Use case         | Event streaming, analytics     | Task queues, RPC            |
| Complexity       | Higher                         | Lower                       |

**When Kafka:** High volume, event streaming, audit log, replay needed.
**When RabbitMQ:** Simple message queuing, task distribution, lower volume.

---

## 9. Real-World Kafka Use Cases

**Uber:**
- Rider request published to Kafka
- Driver matching, pricing, notification services all consume

**Netflix:**
- User activity events (what you watched)
- Analytics, recommendations, monitoring all consume

**E-commerce:**
- OrderPlaced event → Payment, Inventory, Email, Analytics all react

**Log Aggregation:**
- All services publish logs to Kafka
- Centralized log processing

---

## 10. Important Kafka Interview Questions

**Q: What is Kafka and why is it used?**
A: Distributed event streaming platform. Used for high-throughput,
   real-time data pipelines. Services publish events; multiple consumers react.

**Q: What is a Consumer Group?**
A: Group of consumers sharing the work of consuming a topic.
   Each partition consumed by exactly one consumer in group.
   Allows parallel processing.

**Q: What is an offset?**
A: Position/index of a message in a partition.
   Consumers track offset to know what they've processed.

**Q: What happens if a consumer crashes?**
A: If offset not committed, consumer reads same messages again.
   This is at-least-once delivery (possible duplicates).
   For exactly-once: use idempotent consumers.

**Q: How does Kafka achieve fault tolerance?**
A: Replication. Each partition copied to multiple brokers.
   If leader fails, replica becomes new leader.

**Q: Kafka vs RabbitMQ?**
A: Kafka: high throughput, stores messages, replay possible.
   RabbitMQ: simpler, deletes after consumption, lower throughput.
   Choose Kafka for event streaming; RabbitMQ for task queues.

**Q: How do you ensure message ordering?**
A: Use message keys. Same key → same partition → ordered.
   Order only guaranteed within a partition.

**Q: What is retention in Kafka?**
A: How long Kafka stores messages. Default 7 days.
   Consumers can replay old events within retention window.

---

## 11. Memory Trick
```
Kafka = News Broadcasting System
Producer = Journalist (writes news)
Topic = TV Channel (sports, news, weather)
Partition = Multiple TV towers broadcasting same channel
Broker = TV Transmission tower
Consumer = Viewer watching TV
Consumer Group = Household watching TV (one show, multiple viewers)
Offset = Which episode you last watched
Retention = How long show is available to watch again
```

---

# ════════════════════════════════════════════
# PART 8 — CI/CD & DEPLOYMENT
# ════════════════════════════════════════════

## 1. What is CI/CD?

**Simple definition:**
CI/CD automates the process of taking your code from "written" to "in production".

```
Write Code → Commit → AUTO: Test → AUTO: Build → AUTO: Deploy
```

**CI = Continuous Integration**
Every code commit triggers automatic testing and building.
"Integrate" code changes frequently, detect problems early.

**CD = Continuous Delivery**
Automatically prepare code for release. Deploy to staging automatically.
Production deployment may need manual approval.

**CD = Continuous Deployment**
Automatically deploy to PRODUCTION after all checks pass. No human needed.

---

## 2. Why CI/CD?

Without CI/CD:
- Manual testing takes days
- Manual deployments are error-prone
- Releases are stressful, risky events
- Bugs found late, expensive to fix

With CI/CD:
- Bugs caught immediately
- Deploys are automated and consistent
- Releases are small and frequent (less risk)
- Developers get fast feedback

---

## 3. Typical CI/CD Pipeline

```
Developer pushes code to GitHub
         |
    CI Pipeline triggered
         |
    ┌────┴────┐
    │  BUILD  │  ← compile code, create Docker image
    └────┬────┘
         |
    ┌────┴────┐
    │  TEST   │  ← unit tests, integration tests, security scan
    └────┬────┘
         |
    ┌────┴────┐
    │  PUSH   │  ← push Docker image to ECR/Docker Hub
    └────┬────┘
         |
    ┌─────┴──────┐
    │   DEPLOY   │  ← deploy to staging/production
    └────────────┘
```

---

## 4. GitHub Actions

CI/CD built into GitHub. Define pipelines as YAML files.

```yaml
name: CI/CD Pipeline
on:
  push:
    branches: [main]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Build Docker Image
        run: docker build -t myapp:${{ github.sha }} .
      - name: Run Tests
        run: docker run myapp:${{ github.sha }} npm test
      - name: Deploy to ECS
        run: ./deploy.sh
```

---

## 5. Jenkins

Most popular open-source CI/CD tool. More control, more complexity.

```groovy
pipeline {
    agent any
    stages {
        stage('Build') { steps { sh 'docker build -t myapp .' } }
        stage('Test')  { steps { sh 'npm test' } }
        stage('Deploy'){ steps { sh './deploy.sh' } }
    }
}
```

---

## 6. Deployment Strategies

### Rolling Deployment (default)
Gradually replace old instances with new ones.
```
[v1][v1][v1][v1] → [v1][v1][v1][v2] → [v1][v1][v2][v2] → [v2][v2][v2][v2]
```
✅ No extra servers needed
✅ Zero downtime
❌ Brief mix of old/new versions
❌ Rollback is slow

### Blue-Green Deployment
Run TWO identical environments (Blue=current, Green=new).
Switch traffic from Blue to Green all at once.
```
Users → Load Balancer → BLUE (v1) [live]
                      → GREEN (v2) [standby]

Switch:
Users → Load Balancer → BLUE (v1) [standby]
                      → GREEN (v2) [live]
```
✅ Instant rollback (switch back to Blue)
✅ Zero downtime
❌ Double the server costs during deployment

### Canary Deployment
Send a SMALL percentage (5-10%) of traffic to new version.
If no issues, gradually increase to 100%.
```
100 users → 95% → OLD version
          →  5% → NEW version (canary)

All OK? → 50/50 → All OK? → 100% new
```
✅ Low risk, catch bugs with small % of users
✅ Real traffic testing
❌ Complex to set up
❌ Longer deployment process

---

## 7. Real Production Deployment Flow

```
1. Developer merges PR to main branch
2. GitHub Actions triggered
3. Run unit tests (5 min)
4. Run integration tests (10 min)
5. Security scan (Snyk, SonarQube)
6. Build Docker image
7. Tag with git commit SHA
8. Push to ECR
9. Deploy to STAGING (ECS/K8s)
10. Run smoke tests on staging
11. Manual approval (optional)
12. Deploy to PRODUCTION
13. Monitor metrics/error rates
14. Auto-rollback if error rate spikes
```

---

## 8. Rollback

If deployment goes wrong, go back to previous version.

**Kubernetes:**
```bash
kubectl rollout undo deployment/myapp
```

**ECS:**
Update task definition to previous image tag.

**Blue-Green:**
Switch load balancer back to Blue environment.

---

## 9. Monitoring After Deployment

After deploying, WATCH these metrics:
- Error rate (should not increase)
- Response latency (should not increase)
- CPU/Memory usage
- Business metrics (orders, sign-ups)

Tools: CloudWatch, Datadog, New Relic, Prometheus + Grafana

---

## 10. Important CI/CD Interview Questions

**Q: What is the difference between CI and CD?**
A: CI = automatically test and build on every commit.
   CD = automatically deploy (delivery=manual prod, deployment=auto prod).

**Q: What is Blue-Green deployment?**
A: Two identical environments. Switch all traffic at once.
   Instant rollback by switching back. Costs 2x servers temporarily.

**Q: What is Canary deployment?**
A: Send small % of traffic to new version. Gradually increase if OK.
   Low risk, real traffic testing.

**Q: How do you achieve zero-downtime deployments?**
A: Rolling updates, blue-green, or canary deployment strategies.
   Health checks to ensure new version is working before removing old.

**Q: What do you check after deployment?**
A: Error rates, latency, CPU/memory, business KPIs.
   Watch for at least 15-30 minutes post-deployment.

**Q: How do you handle failed deployments?**
A: Automatic rollback based on health check failures.
   Or manual rollback via previous image tag.

---

# ════════════════════════════════════════════
# PART 9 — DEVOPS & CLOUD BASICS
# ════════════════════════════════════════════

## 1. What is DevOps?

**Simple definition:**
DevOps = Development + Operations working TOGETHER.

Before DevOps: Dev team writes code → throws it over the wall → Ops deploys.
With DevOps: Same team responsible for writing code AND deploying/operating it.

**Goals:**
- Faster releases
- Higher reliability
- Less blame, more collaboration
- Automation everywhere

---

## 2. SDLC (Software Development Life Cycle)

```
Plan → Design → Code → Test → Deploy → Monitor → (back to Plan)
```

**Agile:** Work in short sprints (2 weeks). Deliver working software frequently.
- Sprint planning → Daily standup → Sprint review → Retrospective

---

## 3. Linux Basics (Important for DevOps)

```bash
ls -la              # list files with details
cd /path/to/dir     # change directory
cat file.txt        # show file contents
grep "error" log.txt  # search in file
tail -f app.log     # watch log file live
ps aux              # list all processes
kill PID            # kill process
chmod 755 script.sh # set permissions
curl http://localhost:8080  # HTTP request
netstat -tulpn      # show open ports
df -h               # disk space
free -h             # memory usage
top / htop          # system resources live
```

---

## 4. Networking Basics

### HTTP / HTTPS
HTTP = HyperText Transfer Protocol. How web communication works.
HTTPS = HTTP + SSL encryption.

```
Client sends: GET /api/users HTTP/1.1
Server responds: 200 OK { data: [...] }

Status codes:
2xx = Success (200 OK, 201 Created)
3xx = Redirect (301 Moved, 302 Found)
4xx = Client error (400 Bad Request, 401 Unauthorized, 404 Not Found)
5xx = Server error (500 Internal Error, 503 Service Unavailable)
```

### DNS (Domain Name System)
Translates domain names to IP addresses.
```
google.com → 142.250.80.46
```
Like a phone book for the internet.

### Load Balancer
Distributes traffic across multiple servers.
```
Users → Load Balancer → Server 1
                      → Server 2
                      → Server 3
```
Types: Round Robin, Least Connections, Weighted, Health-check-based.

### Reverse Proxy
A server that sits in front of your servers and forwards requests.
Benefits: SSL termination, caching, hiding backend servers.

Tool: Nginx (most popular reverse proxy).

### CDN (Content Delivery Network)
Servers distributed globally that cache your static content.
User in India gets content from India CDN node, not your US server.
Faster for users worldwide.

### SSL / TLS
Encrypts communication between client and server.
SSL = older. TLS = current (people still say "SSL" but mean TLS).

---

## 5. Monitoring & Observability

### The Three Pillars

**Metrics:** Numbers over time (CPU%, requests/sec, error rate)
**Logs:** Text records of events
**Traces:** Track a request through all services

### Prometheus
Open-source metrics collection tool.
Scrapes metrics from applications every N seconds.
Stores time-series data.

### Grafana
Dashboard/visualization tool.
Reads from Prometheus (or other sources) and creates beautiful graphs.

```
Application → exposes /metrics endpoint
Prometheus → scrapes /metrics every 15 seconds
Grafana → reads Prometheus data → shows dashboard
```

### ELK Stack
**E**lasticsearch + **L**ogstash + **K**ibana

- Logstash: Collect and transform logs
- Elasticsearch: Store and search logs (billions of records, fast search)
- Kibana: Visualize logs, create dashboards

Modern alternative: EFK (Elasticsearch + Fluentd + Kibana)

```
App logs → Fluentd/Logstash → Elasticsearch → Kibana dashboard
```

---

## 6. Cloud Basics

### AWS Key Services
```
Compute:    EC2 (VMs), ECS (containers), Lambda (serverless)
Storage:    S3 (object), EBS (block), EFS (file)
Database:   RDS (SQL), DynamoDB (NoSQL), ElastiCache (Redis)
Network:    VPC, Route53 (DNS), CloudFront (CDN), ELB (load balancer)
Security:   IAM, KMS, Secrets Manager, WAF
Monitoring: CloudWatch (metrics+logs), X-Ray (tracing)
```

### VPC (Virtual Private Cloud)
Your own private network inside AWS.
Subnets: Public (internet-accessible) and Private (internal only).

### IAM (Identity and Access Management)
Control WHO can do WHAT in AWS.
Users, Groups, Roles, Policies.

**Principle of Least Privilege:** Give ONLY the permissions needed. Nothing more.

---

# ════════════════════════════════════════════
# PART 10 — INTERVIEW QUESTIONS BANK
# ════════════════════════════════════════════

## BEGINNER QUESTIONS

1. What is Git? Why is version control important?
2. What is Docker? How is it different from a VM?
3. What is a Dockerfile?
4. What is CI/CD?
5. What is a microservice?
6. What is Kubernetes? Why is it needed?
7. What is Kafka used for?
8. What is Terraform?
9. What is AWS ECS?
10. What are the main HTTP status codes?

## INTERMEDIATE QUESTIONS

1. Explain GitFlow branching strategy.
2. What is Docker multi-stage build and why use it?
3. What is an API Gateway? Why needed in microservices?
4. Explain Blue-Green vs Canary deployment.
5. What is a Kubernetes Deployment vs StatefulSet?
6. What is a Kafka Consumer Group?
7. What is Terraform state file?
8. How does ECS auto-scaling work?
9. What is Circuit Breaker pattern?
10. How do you achieve zero-downtime deployment?

## ADVANCED QUESTIONS

1. How would you debug a pod in CrashLoopBackOff?
2. Explain Kafka replication and leader election.
3. How do you handle Terraform state conflicts in a team?
4. What is SAGA pattern in microservices?
5. How does Kubernetes HPA work internally?
6. Explain distributed tracing and why it's needed.
7. What is etcd and why is it critical?
8. How would you design a CI/CD pipeline for microservices?
9. What is the difference between rolling update and recreate strategy?
10. How do you secure secrets in Kubernetes?

## SENIOR / ARCHITECT LEVEL QUESTIONS

1. Design the deployment architecture for a high-traffic e-commerce system.
2. How would you migrate a monolith to microservices?
3. Design a zero-downtime deployment strategy for a critical payment service.
4. How do you handle database migrations in a microservices deployment?
5. What is your approach to observability in a distributed system?
6. How would you design a multi-region deployment on AWS?
7. Explain the CAP theorem and how it affects microservice design.
8. How do you handle service-to-service authentication?
9. What is your strategy for Kubernetes cluster upgrades?
10. How do you prevent cascading failures in microservices?

## SCENARIO-BASED QUESTIONS

1. "Production is down. 5xx errors spiking. What do you do?"
   → Check load balancer → Check service logs → Check recent deployments
   → Check CPU/memory → Rollback if recent deploy → Escalate if unknown

2. "A pod is stuck in Pending state. Why and how do you fix it?"
   → Check events: kubectl describe pod
   → Possible: insufficient resources, no matching node, image pull error
   → Fix: add resources, fix image name, check node taints

3. "Kafka consumer lag is increasing. Why?"
   → Consumers can't keep up with producers
   → Fix: add more consumers (up to partition count), optimize processing

4. "Terraform apply fails halfway. What now?"
   → Some resources created, some not
   → Check state file, manually import created resources or destroy and retry

5. "Docker image size is 2GB. How to reduce?"
   → Use Alpine base image, multi-stage builds, .dockerignore,
   → Remove dev dependencies, clean apt cache

## DEBUGGING QUESTIONS

1. CrashLoopBackOff → `kubectl logs pod-name --previous` (previous crash logs)
2. ImagePullBackOff → Wrong image name, tag, or registry credentials
3. Pod in Pending → Insufficient resources or unschedulable node
4. 503 from service → No healthy pods matching service selector
5. High Kafka consumer lag → Consumer too slow, add more consumers
6. Terraform state lock → Another apply running, or stale lock — force-unlock

---

# ════════════════════════════════════════════
# PART 11 — IMPORTANT COMPARISONS
# ════════════════════════════════════════════

## Docker vs VM

| Feature       | VM                      | Docker                  |
|--------------|-------------------------|-------------------------|
| Size          | GBs                     | MBs                     |
| Start time    | Minutes                 | Seconds                 |
| OS            | Full OS per VM          | Shared host OS kernel   |
| Isolation     | Strong                  | Process-level           |
| Performance   | Slower (overhead)       | Near-native             |
| Use case      | Full OS isolation       | App packaging/deploying |

## Monolith vs Microservices

| Feature       | Monolith                | Microservices           |
|--------------|-------------------------|-------------------------|
| Codebase      | Single                  | Multiple                |
| Deployment    | All at once             | Independent             |
| Scaling       | All components          | Per-service             |
| Failure       | All-or-nothing          | Isolated                |
| Database      | Shared                  | Per-service             |
| Complexity    | Low initially           | High from start         |
| Team size     | Small                   | Large (multiple teams)  |

## ECS vs Kubernetes

| Feature       | ECS                     | Kubernetes (EKS)        |
|--------------|-------------------------|-------------------------|
| Complexity    | Low                     | High                    |
| AWS-native    | Yes, deeply integrated  | Via EKS                 |
| Multi-cloud   | No                      | Yes                     |
| Learning curve| Low                     | High                    |
| Cost          | Lower overhead          | EKS control plane cost  |
| Features      | Basic                   | Rich ecosystem          |
| Best for      | AWS-focused teams       | Complex, large scale    |

## Kafka vs RabbitMQ

| Feature       | Kafka                   | RabbitMQ                |
|--------------|-------------------------|-------------------------|
| Type          | Event streaming         | Message queue           |
| Throughput    | Millions/sec            | Thousands/sec           |
| Storage       | Days/weeks (configurable)| Until consumed          |
| Replay        | Yes                     | No                      |
| Protocol      | Custom TCP              | AMQP                    |
| Complexity    | Higher                  | Lower                   |
| Use case      | Event streaming, logs   | Task queues, RPC        |

## Docker Swarm vs Kubernetes

| Feature       | Docker Swarm            | Kubernetes              |
|--------------|-------------------------|-------------------------|
| Complexity    | Simple                  | Complex                 |
| Features      | Basic                   | Rich                    |
| Auto-scaling  | No (manual)             | Yes (HPA)               |
| Community     | Smaller, declining      | Huge, growing           |
| Production use| Small setups            | Large enterprises       |

## Terraform vs CloudFormation

| Feature       | Terraform               | CloudFormation          |
|--------------|-------------------------|-------------------------|
| Language      | HCL                     | YAML/JSON               |
| Cloud support | Multi-cloud             | AWS only                |
| State         | External state file     | Managed by AWS          |
| Modules       | Rich registry           | Nested stacks           |
| Community     | Very large              | Large (AWS-specific)    |

## CI vs CD

| Feature       | CI                      | CD                      |
|--------------|-------------------------|-------------------------|
| Stands for    | Continuous Integration  | Continuous Delivery/Deployment |
| When runs     | Every commit            | After CI passes         |
| What it does  | Build + Test            | Deploy to staging/prod  |
| Goal          | Detect issues early     | Automate releases       |

## Rolling vs Blue-Green Deployment

| Feature       | Rolling                 | Blue-Green              |
|--------------|-------------------------|-------------------------|
| Extra servers | No                      | Yes (2x during deploy)  |
| Rollback speed| Slow                    | Instant                 |
| Traffic mix   | Brief old+new           | All-at-once switch      |
| Cost          | Lower                   | Higher                  |
| Risk          | Brief mixed state       | Low (instant rollback)  |

## Pod vs Container

| Feature       | Container               | Pod                     |
|--------------|-------------------------|-------------------------|
| Runtime       | Docker/containerd       | Kubernetes concept      |
| What is it    | Running process         | Wrapper around container|
| Networking    | Own                     | Shared within pod       |
| Storage       | Own                     | Shared within pod       |
| Scaling       | Docker scales containers| K8s scales pods         |

## Service vs Ingress (Kubernetes)

| Feature       | Service                 | Ingress                 |
|--------------|-------------------------|-------------------------|
| Layer         | L4 (TCP/UDP)            | L7 (HTTP/HTTPS)         |
| Routing       | By port                 | By URL path/hostname    |
| SSL           | No (except LoadBalancer)| Yes                     |
| Use case      | Internal service access | External HTTP access    |

---

# ════════════════════════════════════════════
# PART 12 — PRODUCTION SCENARIOS
# ════════════════════════════════════════════

## Scenario 1: High Traffic E-Commerce

```
Architecture:
Internet → CloudFront (CDN)
        → Route53 (DNS)
        → Application Load Balancer
        → ECS/Kubernetes cluster
            → Product Service (3 replicas)
            → Order Service (5 replicas)
            → Payment Service (3 replicas, multi-AZ)
            → Notification Service (2 replicas)
        → Kafka cluster (order events)
        → RDS (PostgreSQL, Multi-AZ)
        → ElastiCache (Redis, sessions + cache)
        → S3 (images, static assets)
```

**CI/CD:** GitHub → GitHub Actions → ECR → ECS Rolling Deploy
**Monitoring:** CloudWatch + Grafana dashboards
**Alerts:** PagerDuty for on-call

## Scenario 2: Zero-Downtime Deployment Strategy

1. Feature branch → PR → Code Review → Merge to main
2. CI: Tests pass, security scan clean
3. Docker image built, tagged with git SHA
4. Pushed to ECR
5. Deploy to STAGING (same as prod)
6. Smoke tests on staging
7. Canary deploy to PROD: 5% traffic to new version
8. Monitor for 15 minutes: error rates, latency
9. Gradually increase: 20% → 50% → 100%
10. Old tasks drained and terminated

## Scenario 3: Kafka-Driven Order Processing

```
1. User places order → Order Service
2. Order Service → Publishes "OrderPlaced" to Kafka
3. Kafka: Topic "orders", 10 partitions
4. Consumers:
   - Payment Service: charges customer
   - Inventory Service: reserves items
   - Email Service: sends confirmation
   - Analytics Service: records for dashboards
5. Payment Service → Publishes "PaymentSucceeded"
6. Fulfillment Service consumes → ships order
```

**Fault Tolerance:** If Email Service is down, orders still process.
Email Service catches up when it comes back (Kafka retains messages).

---

# ════════════════════════════════════════════
# QUICK REVISION NOTES
# ════════════════════════════════════════════

## GIT Quick Ref
- git clone/init → set up repo
- git branch/checkout → work on feature
- git add/commit → save snapshot
- git push/pull → sync with remote
- git merge/rebase → combine branches
- git stash → temp save work
- GitFlow: main → develop → feature/release/hotfix

## DOCKER Quick Ref
- Dockerfile → build image
- docker build / docker run
- Image = blueprint, Container = running instance
- Volume = persistent storage
- Docker Compose = multi-container manager
- Multi-stage = smaller images
- Registry = image storage (ECR, Docker Hub)

## MICROSERVICES Quick Ref
- One service = one responsibility
- Own database per service
- API Gateway = single entry point
- Sync: REST/gRPC | Async: Kafka/RabbitMQ
- Circuit Breaker = stop calling failing service
- Service Discovery = find services dynamically

## ECS Quick Ref
- Task Definition = blueprint
- Task = running container
- Service = manages tasks (keeps N running)
- Fargate = serverless | EC2 = you manage servers
- ECR = private Docker registry on AWS

## TERRAFORM Quick Ref
- init → plan → apply → destroy
- Resources = infrastructure items
- State file = tracks what exists
- Remote state = S3 + DynamoDB lock
- Modules = reusable code blocks

## KUBERNETES Quick Ref
- Pod → Deployment → Service → Ingress
- ConfigMap (config) | Secret (sensitive)
- HPA = auto-scale pods
- Rolling update = zero downtime
- StatefulSet = databases
- DaemonSet = one pod per node
- kubectl = command-line tool

## KAFKA Quick Ref
- Producer → Topic (Partitions) → Consumer Group
- Offset = position in partition
- Retention = messages stored for days
- Replication = fault tolerance
- Consumer Group = parallel consumption

## CI/CD Quick Ref
- CI: test + build on every commit
- CD: deploy automatically
- Rolling → gradual, no extra servers
- Blue-Green → instant rollback, double cost
- Canary → small% test, gradual rollout

## DEVOPS Quick Ref
- Prometheus: scrape metrics
- Grafana: visualize metrics
- ELK/EFK: collect and search logs
- Distributed tracing: Jaeger/Zipkin
- IaC: Terraform/CloudFormation

---

# ════════════════════════════════════════════
# INTERVIEW DAY CHECKLIST
# ════════════════════════════════════════════

## Before Interview
- [ ] Review GitFlow workflow
- [ ] Practice explaining Docker (Image vs Container)
- [ ] Practice explaining Kubernetes (Pod/Service/Deployment)
- [ ] Review Kafka consumer groups and partitions
- [ ] Practice Blue-Green vs Canary explanation
- [ ] Review Terraform plan/apply/state
- [ ] Practice "tell me about a production incident" story

## Common Opening Questions
- "Tell me about your experience with Docker/K8s/CI-CD"
- "Walk me through a deployment you did"
- "How do you handle a production outage?"
- "What is your approach to microservices communication?"

## Key Phrases that Impress Interviewers
- "We used Canary deployment to minimize risk"
- "Circuit breaker pattern prevented cascading failures"
- "We stored Terraform state remotely with S3 + DynamoDB locking"
- "Zero-downtime deployment with rolling updates in Kubernetes"
- "Distributed tracing with Jaeger to debug cross-service issues"
- "Consumer groups allowed us to independently scale services"
- "We followed the principle of least privilege for IAM roles"

---

# END OF GUIDE
# ════════════════════════════════════════════
# GOOD LUCK IN YOUR INTERVIEWS!
# Remember: Understand concepts > Memorize commands
# ════════════════════════════════════════════
ENDOFFILE
echo "File created. Size: $(wc -l /mnt/user-data/outputs/DevOps_Interview_Prep_Guide.md | cut -d' ' -f1) lines"OutputInput validation errors occurred:
description: Field requiredDone
