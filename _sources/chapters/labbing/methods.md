(labbing:methods)=
# Materials and Methods

<hr>

A dedicated {{GitHub}} organization titled "The Labbing Project" (see https://github.com/TheLabbingProject) has been created to centralize development efforts. The following section will detail the technological stack used to build the application.

(labbing:methods:backend)=
## Web Framework

Enabling secure remote access and providing robust infrastructure that can easily be deployed and scaled requires an uncompromising web application development framework. There are a number of Python-native high-level web frameworks (for a comprehensive review, see https://wiki.python.org/moin/WebFrameworks). However, the most popular option (by {{GitHub}} star counts at the time of writing) is {{Django}}.

(labbing:methods:backend:django)=
### Django

{{Django}} (see https://www.djangoproject.com/) is a widely used free and open-source web application development framework with a number of outstanding advantages. It is actively maintained by an independent non-profit organization and used by well-known websites, including [Instagram](https://www.instagram.com/), [Mozilla](https://www.mozilla.org/), [Pinterest](https://www.pinterest.com/), and more (see [Overview](https://www.djangoproject.com/start/overview/) page in the {{Django}} project's website). The framework's architecture promotes a modular design that is easily extensible and reusable. It also excels in database management, and includes a powerful Object-relational mapper ({{ORM}}) which greatly reduces the complexity of database administration and interaction by enabling the representation of data models as simple Python classes. Many aspects of routine web application development, such as web security, user administration, session management, caching, logging, testing, etc., are integrated into the framework in compliance with the highest standards in the field. The documentation site (see https://docs.djangoproject.com/) is exceptionally extensive and offers tutorials and educational content, thereby significantly reducing the learning-curve for potential contributors from the research community. Python's renowned capacity of abstraction and intuitive syntax combined with {{Django}}'s fully-featured, scalable design, grants non-professional programmers unprecedented accessibility to actively participate in high-level web develpment.

{{Django}} web applications are written as a single *project*, providing general application-wide settings and resources, and *apps*, providing some custom, loosly-coupled and reusable functionality (for more information, see the ["Applications"](https://docs.djangoproject.com/en/dev/ref/applications/) and ["Design philosophies"](https://docs.djangoproject.com/en/dev/misc/design-philosophies/) sections in the {{Django}} project's documentation site). This architecture enables the creation of a particularly stable and maintainable foundation by tremendously facilitating the extension, modification, or replacement of different parts as requirements change over time or across deployments.

(labbing:methods:backend:django:api)=
#### Application Programming Interface (API)

{{DRF}} (see https://www.django-rest-framework.org/) was used to generate a {{REST}} {{API}} for the application, exposing comprehensive database management and querying capabilities using simple web requests. In addition, returning generic, {{JSON}}-encoded responses enables flexible interaction with any number of external services or independent user interfaces.

(labbing:methods:backend:database)=
## Database

{{Django}} officially supports a number of databases (see https://docs.djangoproject.com/en/dev/ref/databases/), with {{PostgreSQL}} being a leading choice for applications with higher demands in terms of database performance and flexibility.

(labbing:methods:backend:database:postgresql)=
### PostgreSQL

{{PostgreSQL}} is a free and open-source relational database management system ({{RDBMS}}). It is one of the most popular {{DBMS}}s in general (e.g. see https://db-engines.com/en/ranking), boasting some of the most advanced functionality in terms of both security and performance. {{Django}}'s {{PostgreSQL}} backend uses the psycopg (see https://www.psycopg.org/) Python adapter, which is written mostly in the C programming language, and provides a feature-rich, fast, and secure integration with the application's components.

(labbing:methods:backend:tasks)=
## Task Orchestration

Execution of analytical workflows in a scalable manner requires an advanced, distributed task queuing system. Preprocessing and feature extraction pipelines used in neuroimaging range from simple transformations to exceptionally resource-heavy, long-running tasks. Being able to initialize background processes across threads and machines in batch and monitor progress is a core requirement.

(labbing:methods:backend:tasks:celery)=
### Celery

{{Celery}} is the most popular task queue manager written in Python (by {{GitHub}} stars count at the time of writing). It is free and open-source, actively maintained, in widespread use in industry, and provides native support for integration with {{Django}} projects (see https://docs.celeryproject.org/en/stable/django/). By default, {{Celery}} uses RabbitMQ (see https://www.rabbitmq.com/) to send and receive messages, however, other message brokers such as Redis (see https://redis.io/) and Amazon SQS (see https://aws.amazon.com/sqs/) are also supported.

*django-celery-results* (see https://django-celery-results.readthedocs.io/) and *django-celery-beat* (see https://django-celery-beat.readthedocs.io/) are also enabled by default and complement {{Celery}} with database-integrated task monitoring and support for periodic task scheduling (respectively).

(labbing:methods:backend:distribution)=
## Data Distribution

While the application's {{REST}} {{API}} does provide endpoints for downloading both data instances and analysis results, distributing large collections of files necessitates a more controlled approach.

(labbing:methods:backend:distribution:paramiko)=
### Paramiko

{{Paramiko}} (see https://www.paramiko.org/) is a free and open-source Python implementation of the {{SSH}}v2 protocol. It enables highly controlled {{SFTP}} session negotiation over {{SSH}}, thereby allowing researchers to safely transport files to any {{SSH}} accessible machine.

(labbing:methods:frontend)=
## Front-end Framework

While {{Django}} does include a web templating system (the {{Django}} Template Language, see https://docs.djangoproject.com/en/dev/topics/templates/) allowing for the generation of dynamic web pages, initial attempts to leverage it and maintain the stack as minimal and exclusively Python-dependent as possible have failed to produce satisfactory results. In order for the application to offer a modern and responsive user experience, a dedicated front-end web development framework was deemed necessary.

(labbing:methods:frontend:vuejs)=
### Vue.js

{{VueJS}} is a popular free and open-source {{JavaScript}} framework. It is lightweight, modular, rich in documentation and learning materials, and oriented towards both novice and expert developers. While some familiarity with {{HTML}}, {{CSS}}, and {{JavaScript}} is required, {{VueJS}} greatly simplifies the complexities of rendering web content in a browser. By interacting with the web application's {{API}}, the front-end application offers a convenient graphical user interface ({{GUI}}) for researchers to query and retrieve data and derivatives from the server.