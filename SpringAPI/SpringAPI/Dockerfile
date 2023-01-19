FROM openjdk:19-alpine
RUN apk add gradle
COPY src/main .
COPY settings.gradle .
COPY build.gradle . 
COPY SpringAPI.jar .
CMD ["java", "-jar","SpringAPI.jar"] 

