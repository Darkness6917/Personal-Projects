package com.Gradle;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class controller {
    @RequestMapping("/Foo")
    public String getFoo() {
        return  "Bar";
    }
}
