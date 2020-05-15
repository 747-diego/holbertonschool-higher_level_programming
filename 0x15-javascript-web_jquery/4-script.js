#!/usr/bin/node
// Write a Javascript script that toggles the class of the HTML tag HEADER
// to red (#FF0000) when the user clicks on the tag DIV#toggle_header:
$(function () {
    $('DIV#toggle_header').click(function () {
      $('header').toggleClass('#FF0000 #008000');
    });
  });
