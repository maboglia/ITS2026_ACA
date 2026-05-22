package com.maboglia.film.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

import com.maboglia.film.entities.Film;
import com.maboglia.film.services.FilmService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;



@Controller
@RequestMapping("/mvc/films")
public class FilmMVC {

    @Autowired
    private FilmService service;

    @GetMapping("")
    public String getAll(Model m) {

        m.addAttribute("lista", service.getAll());

        return "tutti_film";
    }


    
    

}
