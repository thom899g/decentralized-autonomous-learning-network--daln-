"""
DALN Configuration Manager
Centralized configuration with validation for the decentralized network.
"""
import os
import json
import logging
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any
from enum import Enum
import yaml
from dotenv import load_dotenv

load_dotenv()

class LearningObjective(Enum):
    """Individual node learning objectives"""
    PRICE_PREDICTION = "price_prediction"
    VOLATILITY_FORECASTING = "volatility_forecasting"
    PATTERN_RECOGNITION = "pattern_recognition"
    RISK_ASSESSMENT = "risk_assessment"
    ARBITRAGE_DETECTION = "arbitrage_detection"

class KnowledgeSharingProtocol(Enum):
    """Secure knowledge sharing mechanisms"""
    FEDERATED_AVERAGING = "federated_averaging"
    KNOWLEDGE_DISTILLATION = "knowledge_distillation"
    DIFFERENTIAL_PRIVACY = "differential_privacy"
    BLOCKCHAIN_ANCHORED = "blockchain_anchored"

@dataclass
class NodeConfig:
    """Individual node configuration"""
    node_id: str
    learning_objectives: List[LearningObjective]
    data_sources: List[str]
    privacy_budget: float = 1.0
    minimum_peers: int = 3
    max_local_epochs: int = 10
    batch_size: int = 32
    knowledge_sharing_protocol: KnowledgeSharingProtocol = KnowledgeSharingProtocol.FEDERATED_AVERAGING
    
    def validate(self) -> bool:
        """Validate node configuration"""
        if not self.node_id:
            raise ValueError("Node ID cannot be empty")
        if not self.learning_objectives:
            raise ValueError("At least one learning objective required")
        if self.privacy_budget <= 0 or self.privacy_budget > 10:
            raise ValueError("Privacy budget must be between 0 and 10")
        if self.minimum_peers < 1:
            raise ValueError("Minimum peers must be at least 1")
        return True

@dataclass
class NetworkConfig:
    """Network-wide configuration"""
    firebase_config: Dict[str, Any]
    p2p_bootstrap_nodes: List[str] = field(default_factory=list)
    model_update_interval: int = 300  # seconds
    knowledge_retention_days: int = 30
    max_message_size: int = 10485760  # 10MB