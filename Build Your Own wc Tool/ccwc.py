#!/usr/bin/env python
import click
import os

@click.command()
@click.option('--c', is_flag=True, help='count bytes of the following file')
@click.option('--l',  is_flag=True, help='count lines of the following file')
@click.option('--w',  is_flag=True, help='count words of the following file')
@click.option('--cc',  is_flag=True, help='count words of the following file')

@click.argument('file', type=click.File('r'))


def main(c, l, w, cc, file):
    """Simple program that to generate various counts of a file"""
    if not file:
        click.echo("No File")
        return
    opened_file = file.read()
    if c:
        click.echo(byteCount(opened_file)) 
    if l:
        click.echo(lineCount(opened_file))
    if w:
        click.echo(wordCount(opened_file))
    if cc:
        click.echo(charCount(opened_file))
    if not (c or l or w or cc):
        click.echo(f"Byte Count: {byteCount(opened_file)}")
        click.echo(f"Word Count: {wordCount(opened_file)}")
        click.echo(f"Line Count: {lineCount(opened_file)}")
        click.echo(f"Character Count: {charCount(opened_file)}")


def byteCount(file_content):
    return len(file_content.encode('utf-8'))

def wordCount(file_content):
   return len(file_content.split())

def lineCount(file_content):
    return len(file_content.split("\n"))

def charCount(file_content):
   return len(file_content)

if __name__ == '__main__':
    main()