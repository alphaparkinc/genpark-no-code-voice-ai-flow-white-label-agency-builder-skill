class NoCodeVoiceAiFlowWhiteLabelAgencyBuilderClient:
    def build_flow(self, industry_vertical: str = "real_estate", agency_branding: dict = None) -> dict:
        agency_branding = agency_branding or {}
        brand_name = agency_branding.get("name", "AgencyBrand")
        templates = {
            "real_estate": ["Lead qualification inbound", "Property showing scheduler", "Open house follow-up outbound"],
            "dental": ["Appointment reminder outbound", "New patient intake inbound", "Insurance verification"],
            "hvac": ["Emergency inbound dispatch", "Seasonal service upsell outbound", "Appointment confirmation"]
        }
        chosen = templates.get(industry_vertical, templates["real_estate"])
        flow = {"industry": industry_vertical, "nodes": [{"id": i+1, "name": n, "type": "voice_node"} for i, n in enumerate(chosen)]}
        pkg = {"brand_name": brand_name, "custom_domain": f"voice.{brand_name.lower().replace(' ','-')}.ai", "reseller_markup_pct": 35, "deployment_ready": True}
        return {"generated_flow": flow, "white_label_package": pkg, "estimated_deployment_minutes": 12}
