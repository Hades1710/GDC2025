# Generated by Django 3.0.5 on 2025-03-26 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0005_auto_20250320_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodrequest',
            name='educational_interest',
            field=models.CharField(blank=True, choices=[('stem', 'STEM (Science, Technology, Engineering, Mathematics)'), ('arts', 'Arts & Humanities (Literature, History, Philosophy, Visual Arts)'), ('business', 'Business & Entrepreneurship'), ('medical', 'Medical & Healthcare Studies'), ('vocational', 'Vocational & Skill-Based Education'), ('sports', 'Sports & Physical Education'), ('music', 'Music & Performing Arts'), ('digital', 'Digital Literacy & Coding')], max_length=20, null=True),
        ),
    ]
