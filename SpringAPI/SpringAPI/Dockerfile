FROM openjdk:19-alpine
RUN apk add gradle
ADD /src/main .
ADD /build/libs .
EXPOSE 8080
ENTRYPOINT ["java", "-jar","SpringAPI-0.0.1-SNAPSHOT.jar"] 