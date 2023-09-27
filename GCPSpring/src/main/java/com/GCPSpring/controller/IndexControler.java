package com.GCPSpring.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

import com.GCPSpring.model.User;

@Controller
public class IndexControler {

    /*
     * DESPLIEGUE DEL MENÚ PRINCIPAL
     */
    @GetMapping("/")
    public String index(){
        return "index";
    }

    /*
     * RESPUESTA DEL FORMULARIO
     */
    @PostMapping("/login")
    public String userLogIn(@ModelAttribute User usuario, Model model){
        System.out.println(
            usuario.getUserName()+"\n"+
            usuario.getPassword()
        );
        model.addAttribute("userName", usuario.getUserName());
        model.addAttribute("password", usuario.getPassword());
        return "welcome";
    }
}
