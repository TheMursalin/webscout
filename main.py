#!/usr/bin/env python3
"""
WebScout - Web Application Vulnerability & Technology Scanner
Author: Mursalin
"""

import argparse
import sys
from webscout.utils.banner import print_banner
from webscout.utils.logger import get_logger
from webscout.scanners.tech_detector import TechDetector
from webscout.scanners.header_analyzer import HeaderAnalyzer
from webscout.scanners.vuln_checker import VulnChecker
from webscout.reporters.report_builder import ReportBuilder

logger = get_logger(__name__)


def parse_args():
    parser = argparse.ArgumentParser(
        prog="webscout",
        description="Web Application Vulnerability & Technology Scanner",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("url", help="Target URL to scan (e.g. https://example.com)")
    parser.add_argument(
        "-o", "--output",
        choices=["json", "html", "text"],
        default="text",
        help="Output format: text (default), json, html",
    )
    parser.add_argument(
        "-f", "--file",
        metavar="FILENAME",
        help="Save report to file (e.g. report.html)",
    )
    parser.add_argument(
        "--no-banner",
        action="store_true",
        help="Suppress the banner",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=10,
        help="Request timeout in seconds (default: 10)",
    )
    parser.add_argument(
        "--user-agent",
        default="WebScout/1.0 (github.com/mursalin/webscout)",
        help="Custom User-Agent string",
    )
    return parser.parse_args()


def run():
    args = parse_args()

    if not args.no_banner:
        print_banner()

    logger.info(f"Starting scan on: {args.url}")

    config = {
        "timeout": args.timeout,
        "user_agent": args.user_agent,
    }

    # Run all scanners
    tech_detector = TechDetector(args.url, config)
    tech_results = tech_detector.scan()

    header_analyzer = HeaderAnalyzer(args.url, config)
    header_results = header_analyzer.scan()

    vuln_checker = VulnChecker(tech_results)
    vuln_results = vuln_checker.check()

    # Build and output report
    builder = ReportBuilder(
        target=args.url,
        tech_results=tech_results,
        header_results=header_results,
        vuln_results=vuln_results,
    )

    report = builder.build(output_format=args.output)

    if args.file:
        builder.save(report, args.file, args.output)
        logger.info(f"Report saved to: {args.file}")
    else:
        print(report)


if __name__ == "__main__":
    run()
