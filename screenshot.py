#!/usr/bin/env python

import subprocess
import time
import asyncio
import logging
import sys
import signal

import pyppeteer


async def main():
    browser = await pyppeteer.launch(args=['--no-sandbox'])
    page = await browser.newPage()
    await page.goto('http://localhost:4000')
    await page.screenshot({'path': '/github/home/screenshot.png'})
    await browser.close()

with subprocess.Popen(['jekyll', 'serve'], cwd='/github/workspace') as p:
    time.sleep(3.0)
    asyncio.get_event_loop().run_until_complete(main())
    p.kill()
