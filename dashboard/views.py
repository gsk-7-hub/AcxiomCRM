from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from customers.models import Customer
from leads.models import Lead
from opportunities.models import Opportunity
from followups.models import FollowUp


@login_required
def dashboard(request):

    context = {
        "total_customers": Customer.objects.count(),
        "total_leads": Lead.objects.count(),
        "total_opportunities": Opportunity.objects.count(),
        "total_followups": FollowUp.objects.count(),

        "total_opportunity_value": sum(
            opportunity.amount
            for opportunity in Opportunity.objects.all()
        ),

        "won_opportunities": Opportunity.objects.filter(
            stage="Won"
        ).count(),
    }

    return render(request, "dashboard/dashboard.html", context)
