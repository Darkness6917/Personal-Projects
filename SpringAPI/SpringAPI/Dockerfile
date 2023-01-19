FROM openjdk:19-alpine
RUN apk add gradle
COPY src/main .
COPY settings.gradle .
COPY build.gradle . 
COPY /build/libs .
CMD ["java", "-jar","SpringAPI-0.0.1-SNAPSHOT.jar"] 

