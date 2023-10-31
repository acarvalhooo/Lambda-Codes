# SumBucketsSizes
If you need fast answers about the size of all your buckets and wait 24 hours for metrics in storage lens isn't viable, you can use the code below. However, if the lambda function exceeds the limit of 15 minutes, you should consider use pagination and threads. Even if this isn't enough, consider a container usage to monitoring.

This code was developed in Python 3.9.
